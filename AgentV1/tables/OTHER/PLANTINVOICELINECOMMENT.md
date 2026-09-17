# DB2ADMIN.PLANTINVOICELINECOMMENT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `PLNINVLINEPLNINVCOMPANYCODE`, `PLNINVLINEPLNINVDIVISIONCODE`, `PLNINVLINEPLANTINVOICECODE`, `PLANTINVOICELINEINVOICELINENO`, `ORIGIN`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 220932

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PLNINVLINEPLNINVCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PLNINVLINEPLNINVDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PLNINVLINEPLANTINVOICECODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PLANTINVOICELINEINVOICELINENO` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 5 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 7 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 8 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PLANTINVOICELINE_COMMENT` | `PLNINVLINEPLNINVCOMPANYCODE`, `PLNINVLINEPLNINVDIVISIONCODE`, `PLNINVLINEPLANTINVOICECODE`, `PLANTINVOICELINEINVOICELINENO` | [`PLANTINVOICELINE`](../OTHER/PLANTINVOICELINE.md) | `PLANTINVOICECOMPANYCODE`, `PLANTINVOICEDIVISIONCODE`, `PLANTINVOICECODE`, `INVOICELINENO` | RESTRICT | `PLANTINVOICELINECOMMENT.PLNINVLINEPLNINVCOMPANYCODE = PLANTINVOICELINE.PLANTINVOICECOMPANYCODE AND PLANTINVOICELINECOMMENT.PLNINVLINEPLNINVDIVISIONCODE = PLANTINVOICELINE.PLANTINVOICEDIVISIONCODE AND PLANTINVOICELINECOMMENT.PLNINVLINEPLANTINVOICECODE = PLANTINVOICELINE.PLANTINVOICECODE AND PLANTINVOICELINECOMMENT.PLANTINVOICELINEINVOICELINENO = PLANTINVOICELINE.INVOICELINENO` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PLANTINVOICELINECOMMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PLNINVLINEPLNINVCOMPANYCODE,
       t.PLNINVLINEPLNINVDIVISIONCODE,
       t.PLNINVLINEPLANTINVOICECODE,
       t.PLANTINVOICELINEINVOICELINENO,
       t.REPORTTYPE,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE,
       t.CANCELED,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.PLANTINVOICELINECOMMENT t
FETCH FIRST 100 ROWS ONLY;
```
