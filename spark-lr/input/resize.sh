howmany=$1;

# Insert header and create file

mkdir -p generated_files;
cat header.csv > "generated_files/"$howmany"mb.csv";

echo "header inserted and file created"

# Expand file to satisfy required size
for (( i=1; i<=$howmany; i++ ))
do
  cat 1mb_headerless.csv >> "generated_files/"$howmany"mb.csv";
done
echo "1mb file concatted $howmany times to create $howmany mb file";
