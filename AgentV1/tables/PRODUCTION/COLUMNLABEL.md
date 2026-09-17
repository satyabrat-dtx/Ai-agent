# DB2ADMIN.COLUMNLABEL

- **Module**: `PRODUCTION` (low confidence — FK neighbourhood: 1 of 1 related tables are PRODUCTION)
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `COLUMNGROUPCOMPANYCODE`, `COLUMNGROUPCODE`, `COLUMNCODE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 1725

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COLUMNGROUPCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `COLUMNGROUPCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `COLUMNCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `LABEL` | CHAR(20) |  |  |  |  |
| 4 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 5 | `ADDWAREHOUSECOLUMN` | SMALLINT | NOT NULL |  |  |  |
| 6 | `WAREHOUSELABEL` | CHAR(20) |  |  |  |  |
| 7 | `ADDRESALLOCATEDCOLUMN` | SMALLINT | NOT NULL |  |  |  |
| 8 | `RESALLOCATEDLABEL` | CHAR(20) |  |  |  |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COLUMNGROUP_COLUMNLABEL` | `COLUMNGROUPCOMPANYCODE`, `COLUMNGROUPCODE` | [`COLUMNGROUP`](../PRODUCTION/COLUMNGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `COLUMNLABEL.COLUMNGROUPCOMPANYCODE = COLUMNGROUP.COMPANYCODE AND COLUMNLABEL.COLUMNGROUPCODE = COLUMNGROUP.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `COLUMNLABEL_COLUMNLABEL` | [`WORKCENTERANDOPERATIONCOLUMNS`](../PRODUCTION/WORKCENTERANDOPERATIONCOLUMNS.md) | `COMPANYCODE`, `COLUMNLABELCOLUMNGROUPCODE`, `COLUMNLABELCOLUMNCODE` | `WORKCENTERANDOPERATIONCOLUMNS.COMPANYCODE = COLUMNLABEL.COLUMNGROUPCOMPANYCODE AND WORKCENTERANDOPERATIONCOLUMNS.COLUMNLABELCOLUMNGROUPCODE = COLUMNLABEL.COLUMNGROUPCODE AND WORKCENTERANDOPERATIONCOLUMNS.COLUMNLABELCOLUMNCODE = COLUMNLABEL.COLUMNCODE` |

## Indexes

- UNIQUE `COLUMNLABEL1` (COLUMNCODE, COLUMNGROUPCODE, COLUMNGROUPCOMPANYCODE, SEQUENCE)
- `COLUMNLABELUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COLUMNGROUPCOMPANYCODE,
       t.COLUMNGROUPCODE,
       t.COLUMNCODE,
       t.LABEL,
       t.SEQUENCE,
       t.ADDWAREHOUSECOLUMN,
       t.WAREHOUSELABEL,
       t.ADDRESALLOCATEDCOLUMN,
       t.RESALLOCATEDLABEL,
       t.ABSUNIQUEID
FROM   DB2ADMIN.COLUMNLABEL t
FETCH FIRST 100 ROWS ONLY;
```
