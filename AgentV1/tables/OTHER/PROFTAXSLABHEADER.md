# DB2ADMIN.PROFTAXSLABHEADER

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `FACTORYCODE`, `CODE`, `EFFECTIVEFROMDATE`, `EFFECTIVETODATE`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 159243

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `FACTORYCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `FACTORYCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CODE` | CHAR(5) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `EFFECTIVEFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 6 | `EFFECTIVETODATE` | DATE | NOT NULL | PK | primary_key |  |
| 7 | `PHYSICALCHALLENGED` | INTEGER | NOT NULL |  |  |  |
| 8 | `REDUCINGCALCULATION` | INTEGER | NOT NULL |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PROFTAXSLABHEADER.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PROFTAXSLABHEADER.COMPANYCODE = DIVISION.COMPANYCODE AND PROFTAXSLABHEADER.DIVISIONCODE = DIVISION.CODE` |
| `PLANT_FACTORY` | `FACTORYCOMPANYCODE`, `FACTORYCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PROFTAXSLABHEADER.FACTORYCOMPANYCODE = PLANT.COMPANYCODE AND PROFTAXSLABHEADER.FACTORYCODE = PLANT.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PROFTAXSLABHEADER_LINE` | [`PROFTAXSLABDETAIL`](../OTHER/PROFTAXSLABDETAIL.md) | `PROFTAXSLABHEADERCOMPANYCODE`, `PROFTAXSLABHEADERDIVISIONCODE`, `PROFTAXSLABHEADERFACTORYCODE`, `PROFTAXSLABHEADERCODE`, `PROFTAXSLABHDREFFROMDATE`, `PROFTAXSLABHDREFFECTIVETODATE` | `PROFTAXSLABDETAIL.PROFTAXSLABHEADERCOMPANYCODE = PROFTAXSLABHEADER.COMPANYCODE AND PROFTAXSLABDETAIL.PROFTAXSLABHEADERDIVISIONCODE = PROFTAXSLABHEADER.DIVISIONCODE AND PROFTAXSLABDETAIL.PROFTAXSLABHEADERFACTORYCODE = PROFTAXSLABHEADER.FACTORYCODE AND PROFTAXSLABDETAIL.PROFTAXSLABHEADERCODE = PROFTAXSLABHEADER.CODE AND PROFTAXSLABDETAIL.PROFTAXSLABHDREFFROMDATE = PROFTAXSLABHEADER.EFFECTIVEFROMDATE AND PROFTAXSLABDETAIL.PROFTAXSLABHDREFFECTIVETODATE = PROFTAXSLABHEADER.EFFECTIVETODATE` |

## Indexes

- `PROFTAXSLABHEADERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.FACTORYCOMPANYCODE,
       t.FACTORYCODE,
       t.CODE,
       t.EFFECTIVEFROMDATE,
       t.EFFECTIVETODATE,
       t.PHYSICALCHALLENGED,
       t.REDUCINGCALCULATION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.PROFTAXSLABHEADER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
