

# Help a Healthcare Hero!

Are you a healthcare hero in need that is struggling to make ends meet? Or are you simply a good samaritan looking to donate to a struggling nurse, allied health professional, ambulance officer or paramedic? Look no further! Simply search a healthcare hero in need and donate!

[Help a Healthcare Hero](https://crowdfunding-back-end1990.fly.dev/projects/)

## How to register:
1. Navigate to https://crowdfunding-back-end1990.fly.dev/users/
2. Enter the following JSON:

```
{
	"username":"<username>",
	"password":"<password>",
	"first_name": "<first name>",
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

## Insomnia:

### A screenshot of Insomnia, demonstrating a successful GET method for any endpoint:

1. GET a list of all users:
![GET users](https://github.com/cdurber90/crowdfunding_back_end/blob/main/images/list-users.png?raw=true)

2. GET a list of all projects:
![GET project](https://github.com/cdurber90/crowdfunding_back_end/blob/main/images/list-projects.png?raw=true)

3. GET a list of all pledges:
![GET pledges](https://github.com/cdurber90/crowdfunding_back_end/blob/main/images/list-pledges.png?raw=true)

### A screenshot of Insomnia, demonstrating a successful POST method for any endpoint:

1. POST a new user:
![POST user](https://github.com/cdurber90/crowdfunding_back_end/blob/main/images/create-user.png?raw=true)

2. POST a new project:
![POST project](https://github.com/cdurber90/crowdfunding_back_end/blob/main/images/create-project.png?raw=true)

3. POST a new pledge:
![POST pledge](https://github.com/cdurber90/crowdfunding_back_end/blob/main/images/create-pledge.png?raw=true)

### A screenshot of Insomnia, demonstrating a token being returned:

![RETURN TOKEN](https://github.com/cdurber90/crowdfunding_back_end/blob/main/images/api-token-auth.png?raw=true)

## API Specification:


| Endpoint      | Method| Body                           | Authentication | Implemented? |
| ------------- | ----- | ---------------------------    | --- | --- |
| /projects/    | `GET `  | List of all project objects    | N | Y |
| /projects/    | `POST`  | Project object without ID      | Y | Y |
| /projects/PK  | `GET`   | Specific project object        | Y | Y |
| /projects/PK  | `PUT`   | Update specific project object | Y | Y |
| /pledges/     | `GET`   | List of all pledge objects     | N | Y |
| /pledges/     | `POST`  | Pledge object without ID       | Y | Y |
| /pledges/PK   | `GET`   | Specific pledge object         | N | Y |
| /pledges/PK   | `PUT`   | Update specific pledge object  | Y | Y |
| /users/       | `GET`   | List of all user obkects       | N | Y |
| /users/       | `POST`  | User object without ID         | N | Y |
| /users/PK     | `GET`   | Specific user object           | N | Y |
| /users/PK     | `PUT`   | Update specific user object    | Y | Y |



## Database Schema:

[Database Schema](https://github.com/cdurber90/crowdfunding_back_end/blob/main/images/Flowchart.png?raw=true)


