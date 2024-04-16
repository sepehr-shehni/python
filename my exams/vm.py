from pyVim import connect
from pyVmomi import vim

def create_vm(vm_name, cpu_count, memory_mb, datastore, network, vm_folder):
    try:
        service_instance = connect.SmartConnectNoSSL(host='your_vcenter_ip',
                                                     user='your_username',
                                                     pwd='your_password')
        
        # Create VM configuration
        vm_config = vim.vm.ConfigSpec()
        vm_config.numCPUs = cpu_count
        vm_config.memoryMB = memory_mb

        # Create disk
        vm_disk = vim.vm.device.VirtualDisk()
        vm_disk.capacityInKB = 1024  # 1GB
        vm_disk.backing = vim.vm.device.VirtualDisk.FlatVer2BackingInfo()
        vm_disk.controllerKey = 1000
        vm_disk.unitNumber = 0
        vm_disk.deviceInfo = vim.Description()
        vm_disk.deviceInfo.label = 'Disk'
        vm_disk.deviceInfo.summary = 'System Disk'

        # Create network adapter
        nic_spec = vim.vm.device.VirtualDeviceSpec()
        nic_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
        nic_spec.device = vim.vm.device.VirtualE1000()
        nic_spec.device.deviceInfo = vim.Description()
        nic_spec.device.deviceInfo.label = 'Network Adapter'
        nic_spec.device.deviceInfo.summary = 'VM Network'
        nic_spec.device.backing = vim.vm.device.VirtualEthernetCard.NetworkBackingInfo()
        nic_spec.device.backing.network = network
        nic_spec.device.backing.deviceName = network.name
        nic_spec.device.connectable = vim.vm.device.VirtualDevice.ConnectInfo()
        nic_spec.device.connectable.startConnected = True
        nic_spec.device.connectable.allowGuestControl = True

        # Attach disk and network adapter to VM configuration
        vm_config.deviceChange = [vim.vm.device.VirtualDeviceSpec(device=vm_disk, operation='add'),
                                  nic_spec]

        # Create VM
        vm_folder.CreateVM_Task(config=vm_config, pool=None, host=None)
        print("VM created successfully.")

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        if service_instance:
            connect.Disconnect(service_instance)

def main():
    vm_name = "MyVirtualMachine"
    cpu_count = 2
    memory_mb = 2048  # 2GB
    datastore_name = "your_datastore_name"
    network_name = "your_network_name"
    vm_folder_name = "your_vm_folder_name"

    service_instance = None
    try:
        service_instance = connect.SmartConnectNoSSL(host='your_vcenter_ip',
                                                     user='your_username',
                                                     pwd='your_password')

        content = service_instance.RetrieveContent()
        datacenter = content.rootFolder.childEntity[0]  # Assuming there is only one datacenter
        vm_folder = datacenter.vmFolder.childEntity[0].vmFolder  # Assuming there is only one folder

        # Find datastore and network by name
        datastore = None
        network = None
        for ds in datacenter.datastoreFolder.childEntity:
            if ds.name == datastore_name:
                datastore = ds
                break
        for nw in datacenter.networkFolder.childEntity:
            if nw.name == network_name:
                network = nw.host[0].network[0]
                break

        if datastore and network:
            create_vm(vm_name, cpu_count, memory_mb, datastore, network, vm_folder)
        else:
            print("Datastore or network not found.")

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        if service_instance:
            connect.Disconnect(service_instance)

if __name__ == "__main__":
    main()
