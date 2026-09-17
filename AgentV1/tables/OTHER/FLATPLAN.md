# DB2ADMIN.FLATPLAN

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 28
- **Primary key**: `COMPANYCODE`, `UPLOADID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 104111

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(8) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `UPLOADID` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `FIRMENGRUPPE` | CHAR(3) |  |  |  |  |
| 3 | `EINNAHMEAUSGABE` | CHAR(1) |  |  |  |  |
| 4 | `BELEGNUMMERUNIQUE` | CHAR(20) |  |  |  |  |
| 5 | `KATEGORIEBEZ` | CHAR(50) |  |  |  |  |
| 6 | `KATEGORIEBEZ2` | CHAR(50) |  |  |  |  |
| 7 | `STATUS` | CHAR(1) |  |  |  |  |
| 8 | `ZAHLDATUM` | DATE |  |  |  |  |
| 9 | `BESTCASEB` | DECIMAL(17,2) |  |  |  |  |
| 10 | `BESTCASEBLW` | DECIMAL(17,2) |  |  |  |  |
| 11 | `PLANVARIANTE` | CHAR(10) |  |  |  |  |
| 12 | `PLANVARIANTEBEZ` | CHAR(50) |  |  |  |  |
| 13 | `BUCHUNGSTEXT` | CHAR(50) |  |  |  |  |
| 14 | `PLANVARIANTEBEZ2` | CHAR(50) |  |  |  |  |
| 15 | `BETRAG` | DECIMAL(17,2) |  |  |  |  |
| 16 | `BETRAGLW` | DECIMAL(17,2) |  |  |  |  |
| 17 | `WORSTCASEB` | DECIMAL(17,2) |  |  |  |  |
| 18 | `WORSTCASEBLW` | DECIMAL(17,2) |  |  |  |  |
| 19 | `KONTONUMMER` | CHAR(10) |  |  |  |  |
| 20 | `KONTOBEZEICHNUNG` | CHAR(50) |  |  |  |  |
| 21 | `KONTOBEZEICHNUNG2` | CHAR(50) |  |  |  |  |
| 22 | `KB` | CHAR(1) |  |  |  |  |
| 23 | `BUCHUNGSDATUM` | DATE |  |  |  |  |
| 24 | `WAEHRUNG` | CHAR(3) |  |  |  |  |
| 25 | `BELEGPOSITION` | CHAR(20) |  |  |  |  |
| 26 | `KATEGORIE` | CHAR(20) |  |  |  |  |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FLATPLANUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.UPLOADID,
       t.FIRMENGRUPPE,
       t.EINNAHMEAUSGABE,
       t.BELEGNUMMERUNIQUE,
       t.KATEGORIEBEZ,
       t.KATEGORIEBEZ2,
       t.STATUS,
       t.ZAHLDATUM,
       t.BESTCASEB,
       t.BESTCASEBLW,
       t.PLANVARIANTE
FROM   DB2ADMIN.FLATPLAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
