# DB2ADMIN.PRODMODCONTROL

- **Module**: `PRODUCTION` (low confidence — FK neighbourhood: 1 of 1 related tables are PRODUCTION)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `PRODDEMANDCODE`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 130520

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PRODDEMANDCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `ORDERNOW` | SMALLINT | NOT NULL |  |  |  |
| 5 | `ORDERMQM` | SMALLINT | NOT NULL |  |  |  |
| 6 | `SPLITNOW` | SMALLINT | NOT NULL |  |  |  |
| 7 | `SPLITMQM` | SMALLINT | NOT NULL |  |  |  |
| 8 | `MODREQNOW` | SMALLINT | NOT NULL |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRODMODCONTROL.COMPANYCODE = COMPANY.CODE` |
| `PRODUCTIONDEMANDTEMPLATE_PRODDEMAND` | `COMPANYCODE`, `PRODDEMANDCODE` | [`PRODUCTIONDEMANDTEMPLATE`](../PRODUCTION/PRODUCTIONDEMANDTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODMODCONTROL.COMPANYCODE = PRODUCTIONDEMANDTEMPLATE.COMPANYCODE AND PRODMODCONTROL.PRODDEMANDCODE = PRODUCTIONDEMANDTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRODMODCONTROLUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PRODDEMANDCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.ORDERNOW,
       t.ORDERMQM,
       t.SPLITNOW,
       t.SPLITMQM,
       t.MODREQNOW,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.PRODMODCONTROL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
