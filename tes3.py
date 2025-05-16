import re
from packaging.version import parse as parse_version

def filter_latest_versions_from_file(input_path='requirements.txt', output_path='requirements_cleaned.txt'):
    latest_versions = {}

    with open(input_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()

            # Bỏ qua dòng rỗng hoặc là link git
            if not line or line.startswith('#') or '@' in line:
                continue

            # Lấy package và version
            match = re.match(r'^([a-zA-Z0-9_\-]+)==([\w\.\+]+)$', line)
            if match:
                pkg, version = match.groups()
                if (pkg not in latest_versions) or (parse_version(version) > parse_version(latest_versions[pkg])):
                    latest_versions[pkg] = version

    # Ghi ra file kết quả
    with open(output_path, 'w', encoding='utf-8') as f:
        for pkg, version in sorted(latest_versions.items()):
            f.write(f"{pkg}=={version}\n")

    print(f"✅ Đã tạo file sạch: {output_path}")

# ▶️ Gọi hàm
filter_latest_versions_from_file()
