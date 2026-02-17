# These and other macros are documented in dhd/droid-hal-device.inc

%define device raphael
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Mi 9T Pro

%define rpm_device raphael

%define installable_zip 1

%define droid_target_aarch64 1

# Skip kernel config verification - kernel already built separately
%define have_kernel_config_checker 0

# Entries migrated from the old rpm/droid-hal-hammerhead.spec
%define enable_kernel_update 1

# Straggler files - device-specific paths that need to be packaged
%define straggler_files \
    /acct \
    /charger \
    /bt_firmware \
    /bugreports \
    /d \
    /cache \
    /sdcard \
    /dsp \
    /firmware \
    /persist \
    /product \
    /odm \
    /system \
    /oem \
    /verity_key \
%{nil}

# Add additional cgroup devices for SM8150
%define add_cgroup_devices /dev/cpuctl /dev/stune

%include rpm/dhd/droid-hal-device.inc
