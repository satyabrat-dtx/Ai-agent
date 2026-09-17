# DB2ADMIN.WORKCENTERANDOPERATIONCOLUMNS

- **Module**: `PRODUCTION` (high confidence — table name starts with 'WORKCENTER')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `COMPANYCODE`, `WORKCENTERCODE`, `OPERATIONCODE`, `COLUMNLABELCOLUMNGROUPCODE`, `COLUMNLABELCOLUMNCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 24142

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `WORKCENTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `OPERATIONCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `COLUMNLABELCOLUMNGROUPCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `COLUMNLABELCOLUMNCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COLUMNLABEL_COLUMNLABEL` | `COMPANYCODE`, `COLUMNLABELCOLUMNGROUPCODE`, `COLUMNLABELCOLUMNCODE` | [`COLUMNLABEL`](../PRODUCTION/COLUMNLABEL.md) | `COLUMNGROUPCOMPANYCODE`, `COLUMNGROUPCODE`, `COLUMNCODE` | RESTRICT | `WORKCENTERANDOPERATIONCOLUMNS.COMPANYCODE = COLUMNLABEL.COLUMNGROUPCOMPANYCODE AND WORKCENTERANDOPERATIONCOLUMNS.COLUMNLABELCOLUMNGROUPCODE = COLUMNLABEL.COLUMNGROUPCODE AND WORKCENTERANDOPERATIONCOLUMNS.COLUMNLABELCOLUMNCODE = COLUMNLABEL.COLUMNCODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `WORKCENTERANDOPERATIONCOLUMNS.COMPANYCODE = COMPANY.CODE` |
| `OPERATION_OPERATION` | `COMPANYCODE`, `OPERATIONCODE` | [`OPERATION`](../PRODUCTION/OPERATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `WORKCENTERANDOPERATIONCOLUMNS.COMPANYCODE = OPERATION.COMPANYCODE AND WORKCENTERANDOPERATIONCOLUMNS.OPERATIONCODE = OPERATION.CODE` |
| `WORKCENTER_WORKCENTER` | `COMPANYCODE`, `WORKCENTERCODE` | [`WORKCENTER`](../PRODUCTION/WORKCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `WORKCENTERANDOPERATIONCOLUMNS.COMPANYCODE = WORKCENTER.COMPANYCODE AND WORKCENTERANDOPERATIONCOLUMNS.WORKCENTERCODE = WORKCENTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `KCENTERANDOPERATIONCOLUMNSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.WORKCENTERCODE,
       t.OPERATIONCODE,
       t.COLUMNLABELCOLUMNGROUPCODE,
       t.COLUMNLABELCOLUMNCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.WORKCENTERANDOPERATIONCOLUMNS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
