<div align="center">

# Instructions for running Flask App.
</div>

The project folder has
<li>
/tests folder - which contains test for all api's
</li>
<li>
/snapshots folder :- which has snapshots of testing all api's
</li>

```For running app in Bash
git clone https://github.com/dvaibhavim/Backend_Flask_app.git
```

### Development

```bash
./compose.sh dev up # Run servers
./compose.sh dev run backend pytest # Run tests
```

### Production

```bash
./compose.sh up # Run servers
./compose.sh run backend pytest # Run tests
```


In dev , it can be accessed at 
<li><b> http://127.0.0.1:5000/songs/ </b></li>

After running test file, the app can be accessed at 
<li><b> http://127.0.0.1:5123/songs/avg/difficulty/ </b></li>