# Django-Zappa
Thisproject is used to show how to deploy an django app on aws lambda using zappa 

# Stack
<ul>
<li>Django</li>
<li>Zapp </li>
<li>virtualenv </li>
<li>S3 </li>
</ul>

## Follow the following steps in order to deploy the app on aws lamba
### 1- Set your virtualmachine(Zappa required a virtual-enviroment in order to work)
<ol>
<li>pip3 install virtualenv</li>
<li>virtualenv -p python3 <desired-path> </li>
<li>source <desired-path>/bin/activate </li>
<li>deactivate </li>
</ol>

### 2-  before running zappa make sure that the following file exist on your machine 
<ul>
<li>vi ~/.aws/credentials </li>
</ul>
The file looks something like this 
```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```