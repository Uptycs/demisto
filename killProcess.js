//+killProcess/killProcess.sh
var filePath = "'"+which("killProcess.sh") +"'";
execute("chmod +x " + filePath, 600);
var output = execute(filePath+" "+args.upt_pid, 600);
