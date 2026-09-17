# DB2ADMIN.BILLOFEXCHANGEDOCUMENTS

- **Module**: `FINANCE` (low confidence — FK neighbourhood: 1 of 1 related tables are FINANCE)
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `BILLOFEXCHANGECOMPANYCODE`, `BILLOFEXCHANGEDIVISIONCODE`, `BILLOFEXCHANGECODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 182096

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BILLOFEXCHANGECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `BILLOFEXCHANGEDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `BILLOFEXCHANGECODE` | CHAR(12) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINENO` | DECIMAL(8,0) | NOT NULL | PK | primary_key |  |
| 4 | `DRAFT` | CHAR(15) |  |  |  |  |
| 5 | `BLAWB` | CHAR(15) |  |  |  |  |
| 6 | `INVOICE` | CHAR(15) |  |  |  |  |
| 7 | `INSURCERTIFICATE` | CHAR(15) |  |  |  |  |
| 8 | `CERTORG` | CHAR(15) |  |  |  |  |
| 9 | `CUSTOMSINV` | CHAR(15) |  |  |  |  |
| 10 | `NOOFCARTONS` | INTEGER | NOT NULL |  |  |  |
| 11 | `PACKINGLIST` | CHAR(15) |  |  |  |  |
| 12 | `INSREPT` | CHAR(15) |  |  |  |  |
| 13 | `GSPCERT` | CHAR(15) |  |  |  |  |
| 14 | `OTHERDOCS` | CHAR(120) |  |  |  |  |
| 15 | `BENCERT` | CHAR(15) |  |  |  |  |
| 16 | `NOOFPCS` | INTEGER | NOT NULL |  |  |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BILLOFEXCHANGE_DOCUMENT` | `BILLOFEXCHANGECOMPANYCODE`, `BILLOFEXCHANGEDIVISIONCODE`, `BILLOFEXCHANGECODE` | [`BILLOFEXCHANGE`](../FINANCE/BILLOFEXCHANGE.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `BILLOFEXCHANGEDOCUMENTS.BILLOFEXCHANGECOMPANYCODE = BILLOFEXCHANGE.COMPANYCODE AND BILLOFEXCHANGEDOCUMENTS.BILLOFEXCHANGEDIVISIONCODE = BILLOFEXCHANGE.DIVISIONCODE AND BILLOFEXCHANGEDOCUMENTS.BILLOFEXCHANGECODE = BILLOFEXCHANGE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BILLOFEXCHANGEDOCUMENTSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.BILLOFEXCHANGECOMPANYCODE,
       t.BILLOFEXCHANGEDIVISIONCODE,
       t.BILLOFEXCHANGECODE,
       t.LINENO,
       t.DRAFT,
       t.BLAWB,
       t.INVOICE,
       t.INSURCERTIFICATE,
       t.CERTORG,
       t.CUSTOMSINV,
       t.NOOFCARTONS,
       t.PACKINGLIST
FROM   DB2ADMIN.BILLOFEXCHANGEDOCUMENTS t
FETCH FIRST 100 ROWS ONLY;
```
