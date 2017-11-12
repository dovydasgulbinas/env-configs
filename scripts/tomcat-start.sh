tomcatdir='/Users/hermes/Libs/Tomcat_TEST'
export JAVA_OPTS="-Djava.security.auth.login.config='$tomcatdir/conf/jaas.conf' -Dorg.apache.el.parser.COERCE_TO_ZERO=false"
#Start tommy catty
$tomcatdir/bin/catalina.sh run

#Stop tommy catty
#/Users/hermes/Libs/Tomcat_TEST/bin/catalina.sh stop
#ln -s /Users/hermes/Projects/erpx-lithuania/out/artifacts/erpx_richf_1_2_war_exploded test-lt

