#!/usr/bin/env python3

DNA = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG'

print('DNA lenght is', len(DNA))

print('I have', DNA.count('A'), 'A')

print('I have', DNA.count('T'), 'T')

print('I have', DNA.count('G'), 'G')

print('I have', DNA.count('C'), 'C')

bird = 'chicken'

print(bird.upper())

dna = 'GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGccccTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACttttCG'

dna_upper = dna.upper()

print('I have', dna_upper.count('A'), 'A')

print('I have', dna_upper.count('T'), 'T')

print('I have', dna_upper.count('G'), 'G')

print('I have', dna_upper.count('C'), 'C')

# I can also do it this way without changing to capital letters:

print('I have', dna.count('A') + dna.count('a'), 'A')

print('I have', dna.count('T') + dna.count('t'), 'T')


# nested replace

rna = (dna.replace('T','U')).replace('t', 'U')

print('I have', rna.count('U'), 'U in rna')


# test
test_dna = 'AATTGGCCA'

print(test_dna.count('A')+test_dna.count('T'), "it's my AT content in test_dna")

print(test_dna.count('A'),"it's my A content in test_dna and", test_dna.count('T'), "it's my T content in test_dna")

# AT content 


AT_DNA_count = DNA.count('A')+DNA.count('T')

#print(DNA.count('A'),"it's my A content in test_dna and", DNA.count('T'), "it's my T content in test_dna")

AT_content= ((AT_DNA_count/ len(DNA)) * 100)

print('{:.2f}'.format(AT_content), "it's my AT content in DNA")


# CG content

GC_DNA_count = DNA.count('G')+DNA.count('C')

GC_content= ((GC_DNA_count/ len(DNA)) * 100)

print('{:.2f}'.format(GC_content), "it's my GC content in DNA")



#substring 


# print(test_dna[3:6]) # gives me TGG so it takes from position 4, I need to specify 99-199

sub_DNA = DNA[99:199]

print(len(sub_DNA))

print(sub_DNA.count('G'))

sub_dna = dna[99:199]

print(len(sub_dna))

print(sub_dna.count('G')+sub_dna.count('g'))

# complemente and reverse complement and 
reverse_sub_DNA = sub_DNA[::-1]

# complement 

complement_DNA_Atot = sub_DNA.replace('A', 't')
complement_DNA_Ttoa = complement_DNA_Atot.replace('T', 'a')
complement_DNA_Gtoc = complement_DNA_Ttoa.replace('G', 'c')
complement_DNA_Ctog = complement_DNA_Gtoc.replace('C', 'g')
complement_DNA = complement_DNA_Ctog.upper()

# reverse complement
reverse_complement_DNA_Atot = reverse_sub_DNA.replace('A', 't')
reverse_complement_DNA_Ttoa = reverse_complement_DNA_Atot.replace('T', 'a')
reverse_complement_DNA_Gtoc = reverse_complement_DNA_Ttoa.replace('G', 'c')
reverse_complement_DNA_Ctog = reverse_complement_DNA_Gtoc.replace('C', 'g')
reverse_complement_DNA = reverse_complement_DNA_Ctog.upper()

print("Original   Sequence 5' {:>110}".format(sub_DNA) + " 3'")
print("Complement Sequence 5' {:>110}".format(complement_DNA) + " 3'")
print("Reverse    Sequence 5' {:>110}".format(reverse_sub_DNA) + " 3'")
print("Reverse  Complement 5' {:>110}".format(reverse_complement_DNA) + " 3'")





