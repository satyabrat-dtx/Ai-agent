# DB2ADMIN.BIEMBROIDERY

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 34103

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(100) |  |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `BIEMBROIDERY.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `BIEMBROIDERY_BACKEMBROIDERY` | [`BICUSTOMEMBELLISHMENTS`](../OTHER/BICUSTOMEMBELLISHMENTS.md) | `COMPANYCODE`, `BACKEMBROIDERYCODE` | `BICUSTOMEMBELLISHMENTS.COMPANYCODE = BIEMBROIDERY.COMPANYCODE AND BICUSTOMEMBELLISHMENTS.BACKEMBROIDERYCODE = BIEMBROIDERY.CODE` |
| `BIEMBROIDERY_FRONTEMBROIDERY` | [`BICUSTOMEMBELLISHMENTS`](../OTHER/BICUSTOMEMBELLISHMENTS.md) | `COMPANYCODE`, `FRONTEMBROIDERYCODE` | `BICUSTOMEMBELLISHMENTS.COMPANYCODE = BIEMBROIDERY.COMPANYCODE AND BICUSTOMEMBELLISHMENTS.FRONTEMBROIDERYCODE = BIEMBROIDERY.CODE` |
| `BIEMBROIDERY_SLEEVEEMBROIDERY` | [`BICUSTOMEMBELLISHMENTS`](../OTHER/BICUSTOMEMBELLISHMENTS.md) | `COMPANYCODE`, `SLEEVEEMBROIDERYCODE` | `BICUSTOMEMBELLISHMENTS.COMPANYCODE = BIEMBROIDERY.COMPANYCODE AND BICUSTOMEMBELLISHMENTS.SLEEVEEMBROIDERYCODE = BIEMBROIDERY.CODE` |

## Indexes

- `BIEMBROIDERYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.BIEMBROIDERY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
