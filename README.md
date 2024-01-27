[Help a Healthcare Hero](https://crowdfunding-back-end1990.fly.dev/projects/)

# Help a Healthcare Hero!

Are you a healthcare hero in need that is struggling to make ends meet? Or are you simply a good samaritan looking to donate to a struggling nurse, allied health professional, ambulance officer or paramedic? Look no further! Simply search a healthcare hero in need and donate!

## How to register:
1. Navigate to https://crowdfunding-back-end1990.fly.dev/users/
2. Enter the following JSON:

```
{
	"username":"<username>",
	"password":"<password>",
	"first_name": "<first name",
	"last_name": "<last name>",
	"email": "<email address>"
}
```
3. Click `Post`

Example:
![Example of creating a new user](https://github.com/cdurber90/crowdfunding_back_end/blob/main/images/create-user.png?raw=true)

## How to donate:
1. Navigate to https://crowdfunding-back-end1990.fly.dev/pledges/
2. Enter the following JSON:

```
{
	"amount": "<insert amount>",
	"comment": "<insert comment>",
	"anonymous": <insert true or false>,
	"project": "<insert unique healthcare hero identifier>",
	"supporter": "<insert unique supporter identifier>"
}
```

3. Click `Post`

Example:
![Example of creating a new pledge](https://github.com/cdurber90/crowdfunding_back_end/blob/main/images/create-pledge.png?raw=true)

## Other project requirements:

[x] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint:

1. GET a list of all users:
!(https://github.com/cdurber90/crowdfunding_back_end/blob/main/images/list-users.png?raw=true)

2. GET a list of all projects:
!(https://github.com/cdurber90/crowdfunding_back_end/blob/main/images/list-projects.png?raw=true)

3. GET a list of all pledges:
!(https://github.com/cdurber90/crowdfunding_back_end/blob/main/images/list-pledges.png?raw=true)

[x] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint:

1. POST a new user:
!(https://github.com/cdurber90/crowdfunding_back_end/blob/main/images/create-user.png?raw=true)

2. POST a new project:
!(https://github.com/cdurber90/crowdfunding_back_end/blob/main/images/create-project.png?raw=true)

3. POST a new pledge:
!(https://github.com/cdurber90/crowdfunding_back_end/blob/main/images/create-pledge.png?raw=true)

[x] A screenshot of Insomnia, demonstrating a token being returned:
!(https://github.com/cdurber90/crowdfunding_back_end/blob/main/images/api-token-auth.png?raw=true)


