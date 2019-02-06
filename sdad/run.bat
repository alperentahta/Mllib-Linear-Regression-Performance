call conda activate spark-lr;


python benchmark.py --core 8  --input input/generated_files/1mb.csv
python benchmark.py --core 7  --input input/generated_files/1mb.csv
python benchmark.py --core 6  --input input/generated_files/1mb.csv
python benchmark.py --core 5  --input input/generated_files/1mb.csv
python benchmark.py --core 4  --input input/generated_files/1mb.csv
python benchmark.py --core 3  --input input/generated_files/1mb.csv
python benchmark.py --core 2  --input input/generated_files/1mb.csv
python benchmark.py --core 1  --input input/generated_files/1mb.csv


python benchmark.py --core 8  --input input/generated_files/10mb.csv
python benchmark.py --core 7  --input input/generated_files/10mb.csv
python benchmark.py --core 6  --input input/generated_files/10mb.csv
python benchmark.py --core 5  --input input/generated_files/10mb.csv
python benchmark.py --core 4  --input input/generated_files/10mb.csv
python benchmark.py --core 3  --input input/generated_files/10mb.csv
python benchmark.py --core 2  --input input/generated_files/10mb.csv
python benchmark.py --core 1  --input input/generated_files/10mb.csv


python benchmark.py --core 8  --input input/generated_files/100mb.csv
python benchmark.py --core 7  --input input/generated_files/100mb.csv
python benchmark.py --core 6  --input input/generated_files/100mb.csv
python benchmark.py --core 5  --input input/generated_files/100mb.csv
python benchmark.py --core 4  --input input/generated_files/100mb.csv
python benchmark.py --core 3  --input input/generated_files/100mb.csv
python benchmark.py --core 2  --input input/generated_files/100mb.csv
python benchmark.py --core 1  --input input/generated_files/100mb.csv

python benchmark.py --core 8  --input input/generated_files/1000mb.csv
python benchmark.py --core 7  --input input/generated_files/1000mb.csv
python benchmark.py --core 6  --input input/generated_files/1000mb.csv
python benchmark.py --core 5  --input input/generated_files/1000mb.csv
python benchmark.py --core 4  --input input/generated_files/1000mb.csv
python benchmark.py --core 3  --input input/generated_files/1000mb.csv
python benchmark.py --core 2  --input input/generated_files/1000mb.csv
python benchmark.py --core 1  --input input/generated_files/1000mb.csv

python benchmark.py --core 8  --input input/generated_files/10000mb.csv
python benchmark.py --core 7  --input input/generated_files/10000mb.csv
python benchmark.py --core 6  --input input/generated_files/10000mb.csv
python benchmark.py --core 5  --input input/generated_files/10000mb.csv
python benchmark.py --core 4  --input input/generated_files/10000mb.csv
python benchmark.py --core 3  --input input/generated_files/10000mb.csv
python benchmark.py --core 2  --input input/generated_files/10000mb.csv
python benchmark.py --core 1  --input input/generated_files/10000mb.csv
