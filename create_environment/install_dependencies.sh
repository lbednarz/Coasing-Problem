# Install dependencies from requirements.txt
while read -r line || [[ -n "$line" ]]; do
    # Trim leading/trailing whitespace from the line
    package=$(echo "$line" | awk '{$1=$1};1')
    # Install the package using pip
    pip install "$package" 
done < requirements.txt

# if this works properly, a '.conda' environment will be created in this folder.