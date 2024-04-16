import nmap

def scan_ports(target):
    # ایجاد یک شیء از کلاس PortScanner
    scanner = nmap.PortScanner()
    
    # اسکن پورت‌ها با استفاده از nmap
    scanner.scan(hosts=target, arguments='-sS -p 111,135,80')
    
    # نمایش نتایج اسکن
    for host in scanner.all_hosts():
        print('Host : %s (%s)' % (host, scanner[host].hostname()))
        print('State : %s' % scanner[host].state())
        for proto in scanner[host].all_protocols():
            print('Protocol : %s' % proto)
            ports = scanner[host][proto].keys()
            for port in ports:
                print('Port : %s\tState : %s' % (port, scanner[host][proto][port]['state']))

# تعیین دستگاه هدف
target = '192.168.10.1'