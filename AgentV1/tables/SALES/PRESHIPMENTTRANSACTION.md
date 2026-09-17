# DB2ADMIN.PRESHIPMENTTRANSACTION

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `PSINVLINEPSINVOICECOMPANYCODE`, `PSINVLINEPSINVOICEDIVISIONCODE`, `PSINVLINEPSINVOICECODE`, `PSINVLINEINVOICELINENO`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 142206

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PSINVLINEPSINVOICECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PSINVLINEPSINVOICEDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PSINVLINEPSINVOICECODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PSINVLINEINVOICELINENO` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `LINENO` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 5 | `LOTCODE` | CHAR(15) |  |  |  |  |
| 6 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 7 | `LENGTH` | DECIMAL(7,2) |  |  |  |  |
| 8 | `WIDTH` | DECIMAL(7,2) |  |  |  |  |
| 9 | `HEIGHT` | DECIMAL(7,2) |  |  |  |  |
| 10 | `REMARKS` | VARCHAR(200) |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PSINVLINE_LINE` | `PSINVLINEPSINVOICECOMPANYCODE`, `PSINVLINEPSINVOICEDIVISIONCODE`, `PSINVLINEPSINVOICECODE`, `PSINVLINEINVOICELINENO` | [`PSINVLINE`](../SALES/PSINVLINE.md) | `PSINVOICECOMPANYCODE`, `PSINVOICEDIVISIONCODE`, `PSINVOICECODE`, `INVOICELINENO` | RESTRICT | `PRESHIPMENTTRANSACTION.PSINVLINEPSINVOICECOMPANYCODE = PSINVLINE.PSINVOICECOMPANYCODE AND PRESHIPMENTTRANSACTION.PSINVLINEPSINVOICEDIVISIONCODE = PSINVLINE.PSINVOICEDIVISIONCODE AND PRESHIPMENTTRANSACTION.PSINVLINEPSINVOICECODE = PSINVLINE.PSINVOICECODE AND PRESHIPMENTTRANSACTION.PSINVLINEINVOICELINENO = PSINVLINE.INVOICELINENO` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRESHIPMENTTRANSACTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PSINVLINEPSINVOICECOMPANYCODE,
       t.PSINVLINEPSINVOICEDIVISIONCODE,
       t.PSINVLINEPSINVOICECODE,
       t.PSINVLINEINVOICELINENO,
       t.LINENO,
       t.LOTCODE,
       t.QUANTITY,
       t.LENGTH,
       t.WIDTH,
       t.HEIGHT,
       t.REMARKS,
       t.CREATIONDATETIME
FROM   DB2ADMIN.PRESHIPMENTTRANSACTION t
FETCH FIRST 100 ROWS ONLY;
```
