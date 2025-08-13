// components/Section.tsx
interface SectionProps {
  children: React.ReactNode;
  className?: string;
}

export default function Section({ children, className = "" }: SectionProps) {
  return (
    <section className={`mx-auto px-6 py-16  ${className}`}>
      {children}
    </section>
  );
}
