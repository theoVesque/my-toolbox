import Link from "next/link";

export default function Home() {
  return (
    <div>
      <h1>Accueil</h1>
      <Link href="/converter">Converter</Link>
    </div>
  );
}
