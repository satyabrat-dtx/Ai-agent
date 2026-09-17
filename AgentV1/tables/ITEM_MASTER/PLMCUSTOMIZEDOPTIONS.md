# DB2ADMIN.PLMCUSTOMIZEDOPTIONS

- **Module**: `ITEM_MASTER` (low confidence — FK neighbourhood: 1 of 1 related tables are ITEM_MASTER)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 215556

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 2 | `COUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 3 | `PROJECTLABEL` | VARCHAR(80) |  |  |  |  |
| 4 | `REASONCONTROLLED` | CHAR(2) | NOT NULL |  |  |  |
| 5 | `VERSIONCHANGEREASONCODE` | CHAR(8) |  | FK | foreign_key |  |
| 6 | `PRODUCTCOPYREASONCODE` | CHAR(8) |  | FK | foreign_key |  |
| 7 | `VERSIONCHANGEEDITABLEENTITY` | SMALLINT | NOT NULL |  |  |  |
| 8 | `DRCOUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `DRCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 10 | `DRCUSTOMIZEUICODE` | CHAR(20) |  |  |  |  |
| 11 | `DRCHECKCODE` | CHAR(20) |  |  |  |  |
| 12 | `LIFECYCLEMANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PLMCUSTOMIZEDOPTIONS.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_COUNTER` | `COUNTERCOMPANYCODE`, `COUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PLMCUSTOMIZEDOPTIONS.COUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND PLMCUSTOMIZEDOPTIONS.COUNTERCODE = COUNTER.CODE` |
| `COUNTER_DRCOUNTER` | `DRCOUNTERCOMPANYCODE`, `DRCOUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PLMCUSTOMIZEDOPTIONS.DRCOUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND PLMCUSTOMIZEDOPTIONS.DRCOUNTERCODE = COUNTER.CODE` |
| `VERSIONCHANGEREASON_PRODUCTCOPYREASON` | `COMPANYCODE`, `PRODUCTCOPYREASONCODE` | [`VERSIONCHANGEREASON`](../ITEM_MASTER/VERSIONCHANGEREASON.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PLMCUSTOMIZEDOPTIONS.COMPANYCODE = VERSIONCHANGEREASON.COMPANYCODE AND PLMCUSTOMIZEDOPTIONS.PRODUCTCOPYREASONCODE = VERSIONCHANGEREASON.CODE` |
| `VERSIONCHANGEREASON_VERSIONCHANGEREASON` | `COMPANYCODE`, `VERSIONCHANGEREASONCODE` | [`VERSIONCHANGEREASON`](../ITEM_MASTER/VERSIONCHANGEREASON.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PLMCUSTOMIZEDOPTIONS.COMPANYCODE = VERSIONCHANGEREASON.COMPANYCODE AND PLMCUSTOMIZEDOPTIONS.VERSIONCHANGEREASONCODE = VERSIONCHANGEREASON.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PLMCUSTOMIZEDOPTIONSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.PROJECTLABEL,
       t.REASONCONTROLLED,
       t.VERSIONCHANGEREASONCODE,
       t.PRODUCTCOPYREASONCODE,
       t.VERSIONCHANGEEDITABLEENTITY,
       t.DRCOUNTERCOMPANYCODE,
       t.DRCOUNTERCODE,
       t.DRCUSTOMIZEUICODE,
       t.DRCHECKCODE
FROM   DB2ADMIN.PLMCUSTOMIZEDOPTIONS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
