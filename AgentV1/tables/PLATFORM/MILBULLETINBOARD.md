# DB2ADMIN.MILBULLETINBOARD

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `BBIDENTIFIER`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 33300

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BBIDENTIFIER` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `BBSTATUS` | INTEGER | NOT NULL |  |  |  |
| 2 | `BBCATEGORY` | INTEGER | NOT NULL |  |  |  |
| 3 | `BBSENDERUSERID` | CHAR(25) |  | FK | foreign_key |  |
| 4 | `BBDATE` | DATE | NOT NULL |  |  |  |
| 5 | `BBEXPIRATIONDATE` | DATE |  |  |  |  |
| 6 | `BBRECIPIENTUSERID` | CHAR(25) |  | FK | foreign_key |  |
| 7 | `BBCSMCSMSUPPLIERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `BBCUSTOMERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 9 | `BBCUSTOMERCUSTOMERSUPPLIERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 10 | `BBTITLE` | VARCHAR(60) | NOT NULL |  |  |  |
| 11 | `BBDETAIL` | LONG VARCHAR |  |  |  |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSUSERDEF_BBRECIPIENT` | `BBRECIPIENTUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `MILBULLETINBOARD.BBRECIPIENTUSERID = ABSUSERDEF.USERID` |
| `ABSUSERDEF_BBSENDER` | `BBSENDERUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `MILBULLETINBOARD.BBSENDERUSERID = ABSUSERDEF.USERID` |
| `ORDERPARTNER_BBCUSTOMER` | `BBCSMCSMSUPPLIERCOMPANYCODE`, `BBCUSTOMERCUSTOMERSUPPLIERTYPE`, `BBCUSTOMERCUSTOMERSUPPLIERCODE` | [`ORDERPARTNER`](../CORE_MASTER/ORDERPARTNER.md) | `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE` | RESTRICT | `MILBULLETINBOARD.BBCSMCSMSUPPLIERCOMPANYCODE = ORDERPARTNER.CUSTOMERSUPPLIERCOMPANYCODE AND MILBULLETINBOARD.BBCUSTOMERCUSTOMERSUPPLIERTYPE = ORDERPARTNER.CUSTOMERSUPPLIERTYPE AND MILBULLETINBOARD.BBCUSTOMERCUSTOMERSUPPLIERCODE = ORDERPARTNER.CUSTOMERSUPPLIERCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `MILBULLETINBOARDUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.BBIDENTIFIER,
       t.BBSTATUS,
       t.BBCATEGORY,
       t.BBSENDERUSERID,
       t.BBDATE,
       t.BBEXPIRATIONDATE,
       t.BBRECIPIENTUSERID,
       t.BBCSMCSMSUPPLIERCOMPANYCODE,
       t.BBCUSTOMERCUSTOMERSUPPLIERTYPE,
       t.BBCUSTOMERCUSTOMERSUPPLIERCODE,
       t.BBTITLE,
       t.BBDETAIL
FROM   DB2ADMIN.MILBULLETINBOARD t
FETCH FIRST 100 ROWS ONLY;
```
