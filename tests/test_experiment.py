import unittest

from PIL import Image

from quantum_experiment_agent.agent import (
    format_experiment_summary,
    is_qaoa_maxcut_request,
    should_submit_hardware,
)
from quantum_experiment_agent.experiment_engine import parse_maxcut_graph, run_maxcut_qaoa


class ExperimentTests(unittest.TestCase):
    def test_routing_and_execution_policy(self):
        local = "Use QAOA to solve Max-Cut on a 5-node graph using the local simulator"
        hardware = "Compare QAOA Max-Cut with real IBM Quantum hardware"
        self.assertTrue(is_qaoa_maxcut_request(local))
        self.assertFalse(should_submit_hardware(local))
        self.assertTrue(should_submit_hardware(hardware))

    def test_explicit_edges(self):
        nodes, edges = parse_maxcut_graph(
            "QAOA Max-Cut for a 4-node graph with edges (0,1), (1,2), (2,3), (3,0)"
        )
        self.assertEqual(nodes, 4)
        self.assertEqual(edges, ((0, 1), (0, 3), (1, 2), (2, 3)))

    def test_qaoa_finds_an_optimal_sample_and_generates_qasm(self):
        result = run_maxcut_qaoa(
            "Use QAOA to solve Max-Cut on a 5-node graph using the local simulator",
            shots=256,
        )
        try:
            self.assertEqual(result.exact_cut, 4)
            self.assertEqual(result.best_cut, result.exact_cut)
            self.assertGreater(result.approximation_ratio, 0.9)
            self.assertEqual(sum(result.counts.values()), 256)
            self.assertIn("OPENQASM 2.0", result.qasm)
            self.assertIn("measure", result.qasm)
            self.assertIn("Approximation ratio", format_experiment_summary(result))
            with Image.open(result.dashboard_path) as image:
                self.assertGreaterEqual(image.width, 2000)
                self.assertGreaterEqual(image.height, 1200)
        finally:
            result.dashboard_path.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
