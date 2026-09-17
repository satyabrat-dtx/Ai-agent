# DB2ADMIN.FINLINETEMPLATEALLOWED

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `FINDOCUMENTTEMPLATECOMPANYCODE`, `FINDOCUMENTTEMPLATECODE`, `LINETEMPLATECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 175569

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINDOCUMENTTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINDOCUMENTTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINETEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `LINETEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `DEFAULTLINETEMPLATE` | SMALLINT | NOT NULL |  |  |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 11 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINLINETEMPLATEALLOWED.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `FINDOCUMENTLINETEMPLATE_LINETEMPLATE` | `LINETEMPLATECOMPANYCODE`, `LINETEMPLATECODE` | [`FINDOCUMENTLINETEMPLATE`](../FINANCE/FINDOCUMENTLINETEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINLINETEMPLATEALLOWED.LINETEMPLATECOMPANYCODE = FINDOCUMENTLINETEMPLATE.COMPANYCODE AND FINLINETEMPLATEALLOWED.LINETEMPLATECODE = FINDOCUMENTLINETEMPLATE.CODE` |
| `FINDOCUMENTTEMPLATE_LINETEMPLATEALLOWED` | `FINDOCUMENTTEMPLATECOMPANYCODE`, `FINDOCUMENTTEMPLATECODE` | [`FINDOCUMENTTEMPLATE`](../FINANCE/FINDOCUMENTTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINLINETEMPLATEALLOWED.FINDOCUMENTTEMPLATECOMPANYCODE = FINDOCUMENTTEMPLATE.COMPANYCODE AND FINLINETEMPLATEALLOWED.FINDOCUMENTTEMPLATECODE = FINDOCUMENTTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINLINETEMPLATEALLOWEDUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINDOCUMENTTEMPLATECOMPANYCODE,
       t.FINDOCUMENTTEMPLATECODE,
       t.LINETEMPLATECOMPANYCODE,
       t.LINETEMPLATECODE,
       t.DEFAULTLINETEMPLATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.OWNINGCOMPANYCODE
FROM   DB2ADMIN.FINLINETEMPLATEALLOWED t
FETCH FIRST 100 ROWS ONLY;
```
