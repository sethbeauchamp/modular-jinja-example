from jinja2 import Environment, FileSystemLoader

vars = {}
vars['vrf'] = input('VRF: ')
vars['customer_type'] = input('Customer Type - OSPF or BGP: ').lower()
vars['rd'] = input('Route Distinguisher: ')
vars['rt'] = input('Route Target: ')

environment = Environment(loader=FileSystemLoader(f'jinja_templates/'))
template = environment.get_template('customer_config.j2')
configuration = template.render(vars=vars)

print()
print(configuration)