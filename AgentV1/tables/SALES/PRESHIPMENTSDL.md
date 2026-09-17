# DB2ADMIN.PRESHIPMENTSDL

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `PSINVOICECOMPANYCODE`, `PSINVOICEDIVISIONCODE`, `PSINVOICECODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 142167

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PSINVOICECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PSINVOICEDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PSINVOICECODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINENO` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 4 | `SDLPROVISIONALCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 5 | `SDLPROVISIONALCODE` | CHAR(15) |  | FK | foreign_key |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PSINVOICE_SDL` | `PSINVOICECOMPANYCODE`, `PSINVOICEDIVISIONCODE`, `PSINVOICECODE` | [`PSINVOICE`](../SALES/PSINVOICE.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `PRESHIPMENTSDL.PSINVOICECOMPANYCODE = PSINVOICE.COMPANYCODE AND PRESHIPMENTSDL.PSINVOICEDIVISIONCODE = PSINVOICE.DIVISIONCODE AND PRESHIPMENTSDL.PSINVOICECODE = PSINVOICE.CODE` |
| `SALESDOCUMENT_SDL` | `PSINVOICECOMPANYCODE`, `SDLPROVISIONALCOUNTERCODE`, `SDLPROVISIONALCODE` | [`SALESDOCUMENT`](../SALES/SALESDOCUMENT.md) | `COMPANYCODE`, `PROVISIONALCOUNTERCODE`, `PROVISIONALCODE` | RESTRICT | `PRESHIPMENTSDL.PSINVOICECOMPANYCODE = SALESDOCUMENT.COMPANYCODE AND PRESHIPMENTSDL.SDLPROVISIONALCOUNTERCODE = SALESDOCUMENT.PROVISIONALCOUNTERCODE AND PRESHIPMENTSDL.SDLPROVISIONALCODE = SALESDOCUMENT.PROVISIONALCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRESHIPMENTSDLUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PSINVOICECOMPANYCODE,
       t.PSINVOICEDIVISIONCODE,
       t.PSINVOICECODE,
       t.LINENO,
       t.SDLPROVISIONALCOUNTERCODE,
       t.SDLPROVISIONALCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PRESHIPMENTSDL t
FETCH FIRST 100 ROWS ONLY;
```
