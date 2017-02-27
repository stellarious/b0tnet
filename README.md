## Installation

    pip install git+https://github.com/<repo_name>

## Usage

    botnet --help
    botnet run --help
    botnet run /path/to/config.json


## Configuration
Config snippets from the module description can be added to the `module_config`
key in the config file. This is the general structure of the config file:

    {
        "modules": ["module_name1", "module_name2"],
        "module_config": {
            "namespace": {
                "module_name": {
                    "config_parameter": "value"
                }
            }
        }
    }

All builtin modules use the namespace `botnet`. Most modules are based on the
`BaseResponder` module, so to change the default command prefix alter the
`module_config.botnet.base_responder.command_prefix` configuration key. See the
example config for details.

## Example config

    {
        "modules": ["irc", "meta"],
        "module_config": {
            "botnet": {
                "irc": {
                    "server": "irc.example.com",
                    "port": 6697,
                    "ssl": true,
                    "nick": "my_bot",
                    "channels": [
                        {
                            "name": "#my-channel",
                            "password": null
                        }
                    ],
                    "autosend": [
                        "PRIVMSG your_nick :I connected!"
                    ]
                },
                "base_responder": {
                    "command_prefix": "!"
                }
            }
        }
    }
