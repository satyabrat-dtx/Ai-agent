# DB2ADMIN.CUTTINGHEADER

- **Module**: `PRODUCTION` (low confidence — FK neighbourhood: 1 of 1 related tables are PRODUCTION)
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `COMPANYCODE`, `COUNTERCODE`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 105215

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 2 | `ITEMTYPEAFICODE` | CHAR(3) |  | FK | foreign_key |  |
| 3 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 4 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `DOCUMENTDATE` | DATE | NOT NULL |  |  |  |
| 7 | `STEPNUMBER` | INTEGER | NOT NULL |  |  |  |
| 8 | `WORKCENTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 9 | `OPERATIONCODE` | CHAR(8) |  | FK | foreign_key |  |
| 10 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 11 | `GROUPED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `GROUPCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 13 | `GROUPCODE` | CHAR(15) |  | FK | foreign_key |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 19 | `PPLIST` | CLOB(24000) |  |  |  |  |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `CUTTINGHEADER.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_COUNTER` | `COUNTERCOMPANYCODE`, `COUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CUTTINGHEADER.COUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND CUTTINGHEADER.COUNTERCODE = COUNTER.CODE` |
| `CUTTINGHEADER_GROUP` | `COMPANYCODE`, `GROUPCOUNTERCODE`, `GROUPCODE` | [`CUTTINGHEADER`](../PRODUCTION/CUTTINGHEADER.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `CUTTINGHEADER.COMPANYCODE = CUTTINGHEADER.COMPANYCODE AND CUTTINGHEADER.GROUPCOUNTERCODE = CUTTINGHEADER.COUNTERCODE AND CUTTINGHEADER.GROUPCODE = CUTTINGHEADER.CODE` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CUTTINGHEADER.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND CUTTINGHEADER.ITEMTYPEAFICODE = ITEMTYPE.CODE` |
| `OPERATION_OPERATION` | `COMPANYCODE`, `OPERATIONCODE` | [`OPERATION`](../PRODUCTION/OPERATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CUTTINGHEADER.COMPANYCODE = OPERATION.COMPANYCODE AND CUTTINGHEADER.OPERATIONCODE = OPERATION.CODE` |
| `WORKCENTER_WORKCENTER` | `COMPANYCODE`, `WORKCENTERCODE` | [`WORKCENTER`](../PRODUCTION/WORKCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CUTTINGHEADER.COMPANYCODE = WORKCENTER.COMPANYCODE AND CUTTINGHEADER.WORKCENTERCODE = WORKCENTER.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `CUTTINGHEADER_GROUP` | [`CUTTINGHEADER`](../PRODUCTION/CUTTINGHEADER.md) | `COMPANYCODE`, `GROUPCOUNTERCODE`, `GROUPCODE` | `CUTTINGHEADER.COMPANYCODE = CUTTINGHEADER.COMPANYCODE AND CUTTINGHEADER.GROUPCOUNTERCODE = CUTTINGHEADER.COUNTERCODE AND CUTTINGHEADER.GROUPCODE = CUTTINGHEADER.CODE` |
| `CUTTINGHEADER_LINE` | [`CUTTINGLINE`](../PRODUCTION/CUTTINGLINE.md) | `CUTTINGHEADERCOMPANYCODE`, `CUTTINGHEADERCOUNTERCODE`, `CUTTINGHEADERCODE` | `CUTTINGLINE.CUTTINGHEADERCOMPANYCODE = CUTTINGHEADER.COMPANYCODE AND CUTTINGLINE.CUTTINGHEADERCOUNTERCODE = CUTTINGHEADER.COUNTERCODE AND CUTTINGLINE.CUTTINGHEADERCODE = CUTTINGHEADER.CODE` |
| `CUTTINGHEADER_CUTTINGDOC` | [`CUTTINGPROGRESS`](../PRODUCTION/CUTTINGPROGRESS.md) | `COMPANYCODE`, `CUTTINGDOCCOUNTERCODE`, `CUTTINGDOCCODE` | `CUTTINGPROGRESS.COMPANYCODE = CUTTINGHEADER.COMPANYCODE AND CUTTINGPROGRESS.CUTTINGDOCCOUNTERCODE = CUTTINGHEADER.COUNTERCODE AND CUTTINGPROGRESS.CUTTINGDOCCODE = CUTTINGHEADER.CODE` |

## Indexes

- `CUTTINGHEADERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.DOCUMENTDATE,
       t.STEPNUMBER,
       t.WORKCENTERCODE,
       t.OPERATIONCODE,
       t.PROGRESSSTATUS,
       t.GROUPED
FROM   DB2ADMIN.CUTTINGHEADER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
