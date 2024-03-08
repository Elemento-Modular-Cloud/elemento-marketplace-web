## FTP documentation

### FTP scructure
The ftp server is composed of the following folders:
- `data` : contains the data of the ftp server
- `passwd` : contains the information of the users in order to handle the authentication


### Test the ftp server
In order to test the ftp server, you can use the following command:
```bash
ftp -p localhost 21
```

### ToDo
- [ ] Check if there is a way to avoid the store of the user information in the `passwd` file or check the robustness of the file