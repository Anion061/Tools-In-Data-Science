mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"21f2000407@student.onlinedegree.iitm.ac.in\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[server]
port = 8080
" > ~/.streamlit/config.toml
