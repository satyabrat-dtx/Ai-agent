# DB2ADMIN.PLANTINVOICECOMMENT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `PLANTINVOICECOMPANYCODE`, `PLANTINVOICEDIVISIONCODE`, `PLANTINVOICECODE`, `ORIGIN`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 218971

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PLANTINVOICECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PLANTINVOICEDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PLANTINVOICECODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 4 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 7 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 8 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PLANTINVOICE_COMMENT` | `PLANTINVOICECOMPANYCODE`, `PLANTINVOICEDIVISIONCODE`, `PLANTINVOICECODE` | [`PLANTINVOICE`](../CORE_MASTER/PLANTINVOICE.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `PLANTINVOICECOMMENT.PLANTINVOICECOMPANYCODE = PLANTINVOICE.COMPANYCODE AND PLANTINVOICECOMMENT.PLANTINVOICEDIVISIONCODE = PLANTINVOICE.DIVISIONCODE AND PLANTINVOICECOMMENT.PLANTINVOICECODE = PLANTINVOICE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PLANTINVOICECOMMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PLANTINVOICECOMPANYCODE,
       t.PLANTINVOICEDIVISIONCODE,
       t.PLANTINVOICECODE,
       t.REPORTTYPE,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE,
       t.CANCELED,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.PLANTINVOICECOMMENT t
FETCH FIRST 100 ROWS ONLY;
```
