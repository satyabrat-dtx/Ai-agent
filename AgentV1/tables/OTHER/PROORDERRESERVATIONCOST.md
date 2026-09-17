# DB2ADMIN.PROORDERRESERVATIONCOST

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `COUNTERCODE`, `CODE`, `COSTNUMBER`, `RESERVATIONLINE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 42090

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `COSTNUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `RESERVATIONLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 5 | `STEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 6 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 7 | `BASEPRIMARYUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 9 | `BASESECONDARYUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 10 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 11 | `USERPACKAGINGUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `WASTETYPE1` | CHAR(2) |  |  |  |  |
| 13 | `WASTE1` | DECIMAL(11,2) |  |  |  |  |
| 14 | `WASTETYPE2` | CHAR(2) |  |  |  |  |
| 15 | `WASTE2` | DECIMAL(11,2) |  |  |  |  |
| 16 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `UNITOFMEASURE_BASEPRIMARYUOM` | `BASEPRIMARYUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `PROORDERRESERVATIONCOST.BASEPRIMARYUOMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_BASESECONDARYUOM` | `BASESECONDARYUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `PROORDERRESERVATIONCOST.BASESECONDARYUOMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_USERPACKAGINGUOM` | `USERPACKAGINGUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `PROORDERRESERVATIONCOST.USERPACKAGINGUOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PROORDERRESERVATIONCOSTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.COSTNUMBER,
       t.RESERVATIONLINE,
       t.STEPNUMBER,
       t.BASEPRIMARYQUANTITY,
       t.BASEPRIMARYUOMCODE,
       t.BASESECONDARYQUANTITY,
       t.BASESECONDARYUOMCODE,
       t.USERPACKAGINGQUANTITY,
       t.USERPACKAGINGUOMCODE
FROM   DB2ADMIN.PROORDERRESERVATIONCOST t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
