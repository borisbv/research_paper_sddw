import os
import shutil
import argparse
import yaml

def package_submission(target_dir):
    dist_dir = os.path.join(target_dir, "dist_submission")
    if os.path.exists(dist_dir):
        shutil.rmtree(dist_dir)
    os.makedirs(dist_dir)

    print(f"Packaging {target_dir} for submission...")

    # Copy and anonymize
    shutil.copytree(os.path.join(target_dir, "sections"), os.path.join(dist_dir, "manuscript"))
    shutil.copytree(os.path.join(target_dir, "figures"), os.path.join(dist_dir, "figures"))
    shutil.copy(os.path.join(target_dir, "references", "references.bib"), os.path.join(dist_dir, "references.bib"))

    # Create anonymized metadata
    with open(os.path.join(target_dir, "metadata.yaml"), 'r') as f:
        meta = yaml.safe_load(f)
        meta['authors'] = ["REDACTED FOR PEER REVIEW"]

    with open(os.path.join(dist_dir, "metadata_anonymized.yaml"), 'w') as f:
        yaml.dump(meta, f)

    print(f"✅ Submission package ready at: {dist_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', required=True)
    args = parser.parse_args()
    package_submission(args.dir)