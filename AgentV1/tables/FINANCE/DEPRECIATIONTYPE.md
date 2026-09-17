# DB2ADMIN.DEPRECIATIONTYPE

- **Module**: `FINANCE` (low confidence — FK neighbourhood: 2 of 2 related tables are FINANCE)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 101203

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(5) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `CALCDEPRECIATIONTYPECODE` | CHAR(20) |  |  |  |  |
| 6 | `DEPRECIATIONMETHOD` | CHAR(2) | NOT NULL |  |  |  |
| 7 | `DEPRECIATIONBASEVALUE` | CHAR(2) |  |  |  |  |
| 8 | `START` | CHAR(2) |  |  |  |  |
| 9 | `LIMIT` | CHAR(2) |  |  |  |  |
| 10 | `DISPOSALRULE` | CHAR(2) |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `DEPRECIATIONTYPE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `DEPRECIATIONTYPE_DEPRECIATIONTYPE` | [`ASSETGROUPVALAREADEFAULTS`](../FINANCE/ASSETGROUPVALAREADEFAULTS.md) | `ASSETGROUPCOMPANYCODE`, `DEPRECIATIONTYPECODE` | `ASSETGROUPVALAREADEFAULTS.ASSETGROUPCOMPANYCODE = DEPRECIATIONTYPE.COMPANYCODE AND ASSETGROUPVALAREADEFAULTS.DEPRECIATIONTYPECODE = DEPRECIATIONTYPE.CODE` |
| `DEPRECIATIONTYPE_DEPRECIATIONTYPE` | [`ASSETVALUATIONAREA`](../FINANCE/ASSETVALUATIONAREA.md) | `ASSETMASTERCOMPANYCODE`, `DEPRECIATIONTYPECODE` | `ASSETVALUATIONAREA.ASSETMASTERCOMPANYCODE = DEPRECIATIONTYPE.COMPANYCODE AND ASSETVALUATIONAREA.DEPRECIATIONTYPECODE = DEPRECIATIONTYPE.CODE` |

## Indexes

- `DEPRECIATIONTYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CALCDEPRECIATIONTYPECODE,
       t.DEPRECIATIONMETHOD,
       t.DEPRECIATIONBASEVALUE,
       t.START,
       t.LIMIT,
       t.DISPOSALRULE,
       t.CREATIONDATETIME
FROM   DB2ADMIN.DEPRECIATIONTYPE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
