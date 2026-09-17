# DB2ADMIN.INVOICETYPEVSDIVISION

- **Module**: `ITEM_MASTER` (low confidence — FK neighbourhood: 1 of 1 related tables are ITEM_MASTER)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `COMPANYCODE`, `ANALYSISCODE`, `DIVISIONCODE`, `INVOICETYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 125197

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ANALYSISCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 3 | `INVOICETYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 8 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 9 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ANALYSISTYPE_ANALYSIS` | `COMPANYCODE`, `ANALYSISCODE` | [`ANALYSISTYPE`](../ITEM_MASTER/ANALYSISTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `INVOICETYPEVSDIVISION.COMPANYCODE = ANALYSISTYPE.COMPANYCODE AND INVOICETYPEVSDIVISION.ANALYSISCODE = ANALYSISTYPE.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `INVOICETYPEVSDIVISION.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `INVOICETYPEVSDIVISION.COMPANYCODE = DIVISION.COMPANYCODE AND INVOICETYPEVSDIVISION.DIVISIONCODE = DIVISION.CODE` |
| `INVOICETYPE_INVOICETYPE` | `COMPANYCODE`, `DIVISIONCODE`, `INVOICETYPECODE` | [`INVOICETYPE`](../SALES/INVOICETYPE.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `INVOICETYPEVSDIVISION.COMPANYCODE = INVOICETYPE.COMPANYCODE AND INVOICETYPEVSDIVISION.DIVISIONCODE = INVOICETYPE.DIVISIONCODE AND INVOICETYPEVSDIVISION.INVOICETYPECODE = INVOICETYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INVOICETYPEVSDIVISIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ANALYSISCODE,
       t.DIVISIONCODE,
       t.INVOICETYPECODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.INVOICETYPEVSDIVISION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
