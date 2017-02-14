#!/usr/bin/env python

import sys, os

# 1: domain_dns
# 2: domain_ocsp
# 3: domain_cdn
# 4: domain_ocsp_dns
# 5: domain_ocsp_cdn
# 6: domain_cdn_dns


def format_csvline(*args):
    line = ",".join(map(str, args))
    line += "\n"
    return line


def domain_dns(domain_dns_fp, dns_collat_fp):
    domain_dns_file = open(domain_dns_fp)
    dns_collat_file = open(dns_collat_fp)

    dns_collat = {}

    collat_fail = 0

    # Populate DNS collat info
    for line in dns_collat_file:
        line = line.strip(',\n\r')
        line = line.split(',')

        # line = [dns, collat]

        try:
            dns = line[0]
            collat = line[1]
        except:
            if collat_fail < 10: print "domain dns collat: " + str(line)
            collat_fail += 1
            continue

        dns_collat[dns] = collat


    dns_collat_file.close()


    # Output rank, domain, dns, collat to file
    output_file = open("results/dns_collat", "w")
    domain_dns_fail = 0
    for line in domain_dns_file:


        line = line.strip(',\n\r')
        line = line.split(',')

        # line = [rank, domain, dns]

        try:
            rank = line[0]
            domain = line[1]
            dns = line[2]
            collat = dns_collat.get(dns)
        except:
            if domain_dns_fail < 10: print "domain dns: " + str(line)
            domain_dns_fail += 1
            continue

        output_line = format_csvline(rank, domain, dns, collat)
        output_file.write(output_line)


    domain_dns_file.close()
    output_file.close()

    print
    print "Collat Failures: " + str(collat_fail)
    print "Domain DNS Failures: " + str(domain_dns_fail)


def domain_ocsp(domain_ocsp_fp, ocsp_collat_fp):
    domain_ocsp_file = open(domain_ocsp_fp)
    ocsp_collat_file = open(ocsp_collat_fp)

    ocsp_collat = {}

    collat_fail = 0

    # Populate OCSP collat info
    for line in ocsp_collat_file:
        line = line.strip(',\n\r')
        line = line.split(',')

        # line = [ocsp, collat]

        try:
            ocsp = line[0]
            collat = line[1]
        except:
            if collat_fail < 10: print "domain ocsp collat" + str(line)
            collat_fail += 1
            continue

        ocsp_collat[ocsp] = collat

    ocsp_collat_file.close()


    # Output rank, domain, ocsp, collat to file
    output_file = open("results/ocsp_collat", "w")
    domain_ocsp_fail = 0
    count = 0
    for line in domain_ocsp_file:

        line = line.strip(',\n\r')
        line = line.split(',')

        # line = [rank, domain, ocsp]

        try:
            rank = line[0]
            domain = line[1]
            ocsp = line[2]
            collat = ocsp_collat.get(ocsp)
        except:
            if domain_ocsp_fail < 10: print "domain ocsp: " + str(line)
            domain_ocsp_fail += 1
            continue

        output_line = format_csvline(rank, domain, ocsp, collat)
        output_file.write(output_line)


    domain_ocsp_file.close()
    output_file.close()

    print
    print "Collat Failures: " + str(collat_fail)
    print "Domain OCSP Failures: " + str(domain_ocsp_fail)


def domain_cdn(domain_cdn_fp, cdn_collat_fp):
    domain_cdn_file = open(domain_cdn_fp)
    cdn_collat_file = open(cdn_collat_fp)

    cdn_collat = {}

    collat_fail = 0

    # Populate cdn collat info
    for line in cdn_collat_file:
        line = line.strip(',\n\r')
        line = line.split(',')

        # line = [cdn, collat]

        try:
            cdn = line[0]
            collat = line[1]
        except:
            if collat_fail < 10: print "domain cdn collat: " + str(line)
            collat_fail += 1
            continue

        cdn_collat[cdn] = collat

    cdn_collat_file.close()


    # Output rank, domain, cdn, collat to file
    output_file = open("results/cdn_collat", "w")
    domain_cdn_fail = 0
    for line in domain_cdn_file:

        line = line.strip(',\n\r')
        line = line.split(',')

        # line = [rank, domain, cdn]

        try:
            rank = line[0]
            domain = line[1]
            cdn = line[2]
            collat = cdn_collat.get(cdn)
        except:
            if domain_cdn_fail < 10: print "domain cdn: " + str(line)
            domain_cdn_fail += 1
            continue

        output_line = format_csvline(rank, domain, cdn, collat)
        output_file.write(output_line)


    domain_cdn_file.close()
    output_file.close()

    print
    print "Collat Failures: " + str(collat_fail)
    print "Domain CDN Failures: " + str(domain_cdn_fail)    


def domain_ocsp_dns(domain_ocsp_fp, ocsp_dns_fp, dns_collat_fp):
    domain_ocsp_file = open(domain_ocsp_fp)
    ocsp_dns_file = open(ocsp_dns_fp)
    dns_collat_file = open(dns_collat_fp)

    dns_collat = {}
    ocsp_dns = {}


    collat_fail = 0

    # Populate DNS collat info
    for line in dns_collat_file:
        line = line.strip(',\n\r')
        line = line.split(',')

        # line = [dns, collat]

        try:
            dns = line[0]
            collat = line[1]
        except:
            if collat_fail < 10: print "domain ocsp dns collat: " + str(line)
            collat_fail += 1
            continue

        dns_collat[dns] = collat

    dns_collat_file.close()


    ocsp_dns_fail = 0

    # Populate OCSP DNS info
    for line in ocsp_dns_file:
        line = line.strip(',\n\r')
        line = line.split(',')

        # line = [ocsp, dns]

        try:
            ocsp = line[0]
            dns = line[1]
        except:
            if ocsp_dns_fail < 10: print "domain ocsp dns info: " + str(line)
            ocsp_dns_fail += 1
            continue

        ocsp_dns[ocsp] = dns

    ocsp_dns_file.close()


    # Output rank, domain, ocsp, dns, collat to file
    output_file = open("results/ocsp_dns_collat", "w")
    domain_ocsp_dns_fail = 0
    for line in domain_ocsp_file:

        line = line.strip(',\n\r')
        line = line.split(',')

        # line = [rank, domain, ocsp]

        try:
            rank = line[0]
            domain = line[1]
            ocsp = line[2]
            dns = ocsp_dns.get(ocsp)
            collat = dns_collat.get(dns)
        except:
            if domain_ocsp_dns_fail < 10: print "domain ocsp dns: " + str(line)
            domain_ocsp_dns_fail += 1
            continue

        output_line = format_csvline(rank, domain, ocsp, dns, collat)
        output_file.write(output_line)

    domain_ocsp_file.close()
    output_file.close()

    print
    print "Collat Failures: " + str(collat_fail)
    print "OCSP DNS Failures: " + str(ocsp_dns_fail)
    print "Domain OCSP Failures: " + str(domain_ocsp_dns_fail)


def domain_ocsp_cdn(domain_ocsp_fp, ocsp_cdn_fp, cdn_collat_fp):
    domain_ocsp_file = open(domain_ocsp_fp)
    ocsp_cdn_file = open(ocsp_cdn_fp)
    cdn_collat_file = open(cdn_collat_fp)

    cdn_collat = {}
    ocsp_cdn = {}


    collat_fail = 0

    # Populate CDN collat info
    for line in cdn_collat_file:
        line = line.strip(',\n\r')
        line = line.split(',')

        # line = [cdn, collat]

        try:
            cdn = line[0]
            collat = line[1]
        except:
            if collat_fail < 10: print "domain ocsp cdn collat: " + str(line)
            collat_fail += 1
            continue

        cdn_collat[cdn] = collat

    cdn_collat_file.close()


    ocsp_cdn_fail = 0

    # Populate OCSP CDN info
    for line in ocsp_cdn_file:
        line = line.strip(',\n\r')
        line = line.split(',')

        # line = [ocsp, cdn]

        try:
            ocsp = line[0]
            cdn = line[1]
        except:
            if ocsp_cdn_fail < 10: print "domain ocsp cdn info: " + str(line)
            ocsp_cdn_fail += 1
            continue

        ocsp_cdn[ocsp] = cdn

    ocsp_cdn_file.close()


    # Output rank, domain, ocsp, cdn, collat to file
    output_file = open("results/ocsp_cdn_collat", "w")
    domain_ocsp_cdn_fail = 0
    for line in domain_ocsp_file:

        line = line.strip(',\n\r')
        line = line.split(',')

        # line = [rank, domain, ocsp]

        try:
            rank = line[0]
            domain = line[1]
            ocsp = line[2]
            cdn = ocsp_cdn.get(ocsp)
            collat = cdn_collat.get(cdn)
        except:
            if domain_ocsp_cdn_fail < 10: print "domain ocsp cdn: " + str(line)
            domain_ocsp_cdn_fail += 1
            continue

        output_line = format_csvline(rank, domain, ocsp, cdn, collat)
        output_file.write(output_line)

    domain_ocsp_file.close()
    output_file.close()

    print
    print "Collat Failures: " + str(collat_fail)
    print "OCSP CDN Failures: " + str(ocsp_cdn_fail)
    print "Domain OCSP Failures: " + str(domain_ocsp_cdn_fail)


def domain_cdn_dns(domain_cdn_fp, cdn_dns_fp, dns_collat_fp):
    domain_cdn_file = open(domain_cdn_fp)
    cdn_dns_file = open(cdn_dns_fp)
    dns_collat_file = open(dns_collat_fp)

    dns_collat = {}
    cdn_dns = {}


    collat_fail = 0

    # Populate dns collat info
    for line in dns_collat_file:
        line = line.strip(',\n\r')
        line = line.split(',')

        # line = [dns, collat]

        try:
            dns = line[0]
            collat = line[1]
        except:
            if collat_fail < 10: print "domain cdn dns collat: " + str(line)
            collat_fail += 1
            continue

        dns_collat[dns] = collat

    dns_collat_file.close()


    cdn_dns_fail = 0

    # Populate cdn dns info
    for line in cdn_dns_file:
        line = line.strip(',\n\r')
        line = line.split(',')

        # line = [cdn, dns]

        try:
            cdn = line[0]
            dns = line[1]
        except:
            if cdn_dns_fail < 10: print "domain cdn dns info: " + str(line)
            cdn_dns_fail += 1
            continue

        cdn_dns[cdn] = dns

    cdn_dns_file.close()


    # Output rank, domain, cdn, dns, collat to file
    output_file = open("results/cdn_dns_collat", "w")
    domain_cdn_dns_fail = 0
    for line in domain_cdn_file:

        line = line.strip(',\n\r')
        line = line.split(',')

        # line = [rank, domain, cdn]

        try:
            rank = line[0]
            domain = line[1]
            cdn = line[2]
            dns = cdn_dns.get(cdn)
            collat = dns_collat.get(dns)
        except:
            if domain_cdn_dns_fail < 10: print "domain cdn dns: " + str(line)
            domain_cdn_dns_fail += 1
            continue

        output_line = format_csvline(rank, domain, cdn, dns, collat)
        output_file.write(output_line)

    domain_cdn_file.close()
    output_file.close()

    print
    print "Collat Failures: " + str(collat_fail)
    print "CDN DNS Failures: " + str(cdn_dns_fail)
    print "Domain CDN Failures: " + str(domain_cdn_dns_fail)


def get_collat(fp, index, collat_d):
    collat_file = open(fp)

    for line in collat_file:
        line = line.strip(',\n\r')
        line = line.split(',')

        rank = line[0]
        domain = line[1]
        collat = line[-1]

        if not domain in collat_d:
            collat_d[domain] = [rank,None,None,None,None,None,None]

        collat_d[domain][index] = collat

    collat_file.close()
    return collat_d


def combine(dns_collat_fp, ocsp_collat_fp, cdn_collat_fp,
            ocsp_dns_collat_fp, ocsp_cdn_collat_fp, cdn_dns_collat_fp):

    collat_d = {}

    dns_collat = get_collat(dns_collat_fp, 1, collat_d)
    ocsp_collat = get_collat(ocsp_collat_fp, 2, collat_d)
    cdn_collat = get_collat(cdn_collat_fp, 3, collat_d)
    ocsp_dns_collat = get_collat(ocsp_dns_collat_fp, 4, collat_d)
    ocsp_cdn_collat = get_collat(ocsp_cdn_collat_fp, 5, collat_d)
    cdn_dns_collat = get_collat(cdn_dns_collat_fp, 6, collat_d)

    output_file = open("results/collat_combined", "w")

    # Populate combined collat dictionary
    for domain in collat_d:
        val = collat_d[domain]

        rank = val[0]
        c1 = val[1]
        c2 = val[2]
        c3 = val[3]
        c4 = val[4]
        c5 = val[5]
        c6 = val[6]

        output_line = format_csvline(rank, domain, c1, c2, c3, c4, c5, c6)
        output_file.write(output_line)

    output_file.close()
    

def main(argv):
    # Parse command line arguments
    if len(sys.argv) < 3:
        print "COMMANDS:\ndomain_dns\ndomain_ocsp\ndomain_cdn\ndomain_ocsp_dns\ndomain_ocsp_cdn\ndomain_cdn_dns\ncombine"
        sys.exit("Usage: ./collat.py <command> <f1> <f2> [f3] ... [f6]")

    command = sys.argv[1]
    file1 = sys.argv[2]
    file2 = sys.argv[3]

    try:
        file3 = sys.argv[4]
        file4 = sys.argv[5]
        file5 = sys.argv[6]
        file6 = sys.argv[7]

    except:
        pass


    # Create results directory if necessary
    dir = os.path.dirname(__file__)
    results_dir = os.path.join(dir, 'results')
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)


    # Execute command
    if command == "domain_dns":
        domain_dns(file1, file2)

    elif command == "domain_ocsp":
        domain_ocsp(file1, file2)

    elif command == "domain_cdn":
        domain_cdn(file1, file2)

    elif command == "domain_ocsp_dns":
        domain_ocsp_dns(file1, file2, file3)

    elif command == "domain_ocsp_cdn":
        domain_ocsp_cdn(file1, file2, file3)

    elif command == "domain_cdn_dns":
        domain_cdn_dns(file1, file2, file3)

    elif command == "combine":
        combine(file1, file2, file3, file4, file5, file6)


    else:
        print "Unknown command."


    print
    print "Execution complete."


if __name__ == "__main__":
    main(sys.argv[1:])