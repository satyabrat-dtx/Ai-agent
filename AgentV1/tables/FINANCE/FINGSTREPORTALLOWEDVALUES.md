# DB2ADMIN.FINGSTREPORTALLOWEDVALUES

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `FINGSTINVOICETAXMAPCOMPANYCODE`, `FINGSTINVOICETAXMAPDIVISIONCOD`, `FINGSTINVOICETAXMAPPOSITION`, `FINGSTINVOICETAXMAPREPORTCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 180169

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINGSTINVOICETAXMAPCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINGSTINVOICETAXMAPDIVISIONCOD` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FINGSTINVOICETAXMAPPOSITION` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `FINGSTINVOICETAXMAPREPORTCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `LINENO` | DECIMAL(18,5) | NOT NULL | PK | primary_key |  |
| 5 | `TRANSACTIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 6 | `TEMPLATE` | CHAR(20) | NOT NULL |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINGSTINVOICETAXMAP_ALLOWEDVALUESDETAIL` | `FINGSTINVOICETAXMAPCOMPANYCODE`, `FINGSTINVOICETAXMAPDIVISIONCOD`, `FINGSTINVOICETAXMAPPOSITION`, `FINGSTINVOICETAXMAPREPORTCODE` | [`FINGSTINVOICETAXMAP`](../FINANCE/FINGSTINVOICETAXMAP.md) | `COMPANYCODE`, `DIVISIONCODE`, `POSITION`, `REPORTCODE` | RESTRICT | `FINGSTREPORTALLOWEDVALUES.FINGSTINVOICETAXMAPCOMPANYCODE = FINGSTINVOICETAXMAP.COMPANYCODE AND FINGSTREPORTALLOWEDVALUES.FINGSTINVOICETAXMAPDIVISIONCOD = FINGSTINVOICETAXMAP.DIVISIONCODE AND FINGSTREPORTALLOWEDVALUES.FINGSTINVOICETAXMAPPOSITION = FINGSTINVOICETAXMAP.POSITION AND FINGSTREPORTALLOWEDVALUES.FINGSTINVOICETAXMAPREPORTCODE = FINGSTINVOICETAXMAP.REPORTCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINGSTREPORTALLOWEDVALUESUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINGSTINVOICETAXMAPCOMPANYCODE,
       t.FINGSTINVOICETAXMAPDIVISIONCOD,
       t.FINGSTINVOICETAXMAPPOSITION,
       t.FINGSTINVOICETAXMAPREPORTCODE,
       t.LINENO,
       t.TRANSACTIONTYPE,
       t.TEMPLATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.FINGSTREPORTALLOWEDVALUES t
FETCH FIRST 100 ROWS ONLY;
```
