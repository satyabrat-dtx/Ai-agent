# DB2ADMIN.REPORTTAX

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 123408

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `REPORTTAX.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `REPORTTAX_LINE` | [`REPTAXDET`](../SALES/REPTAXDET.md) | `REPORTTAXCOMPANYCODE`, `REPORTTAXDIVISIONCODE`, `REPORTTAXCODE` | `REPTAXDET.REPORTTAXCOMPANYCODE = REPORTTAX.COMPANYCODE AND REPTAXDET.REPORTTAXDIVISIONCODE = REPORTTAX.DIVISIONCODE AND REPTAXDET.REPORTTAXCODE = REPORTTAX.CODE` |
| `REPORTTAX_LINE1` | [`REPORTTAXDEFINITIONRPT`](../OTHER/REPORTTAXDEFINITIONRPT.md) | `REPORTTAXCOMPANYCODE`, `REPORTTAXDIVISIONCODE`, `REPORTTAXCODE` | `REPORTTAXDEFINITIONRPT.REPORTTAXCOMPANYCODE = REPORTTAX.COMPANYCODE AND REPORTTAXDEFINITIONRPT.REPORTTAXDIVISIONCODE = REPORTTAX.DIVISIONCODE AND REPORTTAXDEFINITIONRPT.REPORTTAXCODE = REPORTTAX.CODE` |

## Indexes

- `REPORTTAXUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.REPORTTAX t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
