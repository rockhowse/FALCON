import falcon_kit.stats_preassembly as M
import helpers
from cStringIO import StringIO

def test_stats_dict():
    #Stats = collections.namedtuple('FastaStats', ['nreads', 'total', 'n50', 'p95'])
    stats_raw_reads = M.Stats(100, 1000, 50, 95)
    stats_seed_reads = M.Stats(50, 500, 25, 40)
    stats_corrected_reads = M.Stats(10, 100, 5, 9)
    genome_length = 19
    length_cutoff = 10
    frag = 1.0
    trunc = 2.5

    result = M.stats_dict(stats_raw_reads, stats_seed_reads, stats_corrected_reads, genome_length, length_cutoff, frag, trunc)
    expected = {
 'genome_length': 19,
 'length_cutoff': 10,
 'preassembled_bases': 100,
 'preassembled_coverage': 5.263,
 'preassembled_mean': 10.0,
 'preassembled_n50': 5,
 'preassembled_p95': 9,
 'preassembled_reads': 10,
 'preassembled_seed_fragmentation': 1.0,
 'preassembled_seed_truncation': 2.5,
 'preassembled_yield': 0.2,
 'raw_bases': 1000,
 'raw_coverage': 52.632,
 'raw_mean': 10.0,
 'raw_n50': 50,
 'raw_p95': 95,
 'raw_reads': 100,
 'seed_bases': 500,
 'seed_coverage': 26.316,
 'seed_mean': 10.0,
 'seed_n50': 25,
 'seed_p95': 40,
 'seed_reads': 50}
    helpers.equal_dict(result, expected)
