# nuts Cisco IOSXE Test Class

This is an example of how to create a custom test class to be used with [nuts](https://github.com/INSRapperswil/nuts).

## Install

```
pip install git+https://github.com/briantsaunders/nuts-cisco-iosxe-tests.git
```

## Use in Your Tests

To use this custom test class with your tests you will need to reference it in your test bundle.  Below is an example:

```yaml
---
- test_module: nuts_cisco_iosxe_tests.ntp_status
  test_class: TestNtpStatus
  label: NTP Tests
  test_data:
    - host: br-edge-01a
      ntp_status: synchronized
```