export function Footer() {
  return (
    <footer className="bg-slate-900 text-slate-500 py-6 text-center text-sm border-t border-slate-800">
      <p>&copy; {new Date().getFullYear()} AI MemeGen. Built for academic demonstration.</p>
      <p className="mt-1 text-xs">
        Powered by simulated NLP Logic &bull; React Frontend &bull; Python Backend (Reference)
      </p>
    </footer>
  );
}
