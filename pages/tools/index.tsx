// pages/tools.js
import Link from "next/link";
import PageLayout from "../pageLayout";
import MathematicsLayout from "@/components/tools/layout/mathematicsLayout";
export default function Tools() {
  return (
    <PageLayout>
      <h1 className="text-3xl uppercase font-bold	mt-4">Tools</h1>
      <MathematicsLayout />
      <Link
        href="/tools/qrcode/generate"
        className="bg-dark_blue text-white px-4 py-2 rounded-lg content-center"
      >
        {" "}
        QR Code
      </Link>
    </PageLayout>
  );
}
