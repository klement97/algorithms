from common import profile


@profile
def solution(dna, starting_positions, ending_positions):
    nucleotide_impact = {
        'A': 1,
        'C': 2,
        'G': 3,
        'T': 4,
    }
    queries = []
    for start, end in zip(starting_positions, ending_positions):
        sequence = dna[start:end + 1]

        # Iterate through the 4 nucleotides which are sorted by their impact.
        # Once we find the first nucleotide which is in sequence, it is the minimum impact.
        for nucleotide, impact in nucleotide_impact.items():
            if nucleotide in sequence:
                queries.append(impact)
                break

    return queries
