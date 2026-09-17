# DB2ADMIN.STATUSRULE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `ARTICLESTATUSCOMPANYCODE`, `ARTICLESTATUSITEMTYPECODE`, `ARTICLESTATUSCODE`, `LINENR`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 190743

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ARTICLESTATUSCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ARTICLESTATUSITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ARTICLESTATUSCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINENR` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 5 | `ISPROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 6 | `MANAGEKEY1` | SMALLINT | NOT NULL |  |  |  |
| 7 | `MANAGEKEY2` | SMALLINT | NOT NULL |  |  |  |
| 8 | `MANAGEKEY3` | SMALLINT | NOT NULL |  |  |  |
| 9 | `MANAGEKEY4` | SMALLINT | NOT NULL |  |  |  |
| 10 | `MANAGEKEY5` | SMALLINT | NOT NULL |  |  |  |
| 11 | `MANAGEKEY6` | SMALLINT | NOT NULL |  |  |  |
| 12 | `MANAGEKEY7` | SMALLINT | NOT NULL |  |  |  |
| 13 | `MANAGEKEY8` | SMALLINT | NOT NULL |  |  |  |
| 14 | `MANAGEKEY9` | SMALLINT | NOT NULL |  |  |  |
| 15 | `MANAGEKEY10` | SMALLINT | NOT NULL |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ARTICLESTATUS_STATUSRULELIST` | `ARTICLESTATUSCOMPANYCODE`, `ARTICLESTATUSITEMTYPECODE`, `ARTICLESTATUSCODE` | [`ARTICLESTATUS`](../OTHER/ARTICLESTATUS.md) | `COMPANYCODE`, `ITEMTYPECODE`, `CODE` | RESTRICT | `STATUSRULE.ARTICLESTATUSCOMPANYCODE = ARTICLESTATUS.COMPANYCODE AND STATUSRULE.ARTICLESTATUSITEMTYPECODE = ARTICLESTATUS.ITEMTYPECODE AND STATUSRULE.ARTICLESTATUSCODE = ARTICLESTATUS.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `STATUSRULE_STATUSRULECOMBINATIONLIST` | [`STATUSRULECOMBINATION`](../OTHER/STATUSRULECOMBINATION.md) | `COMPANYCODE`, `ITEMTYPECODE`, `STATUSCODE`, `LINENR` | `STATUSRULECOMBINATION.COMPANYCODE = STATUSRULE.ARTICLESTATUSCOMPANYCODE AND STATUSRULECOMBINATION.ITEMTYPECODE = STATUSRULE.ARTICLESTATUSITEMTYPECODE AND STATUSRULECOMBINATION.STATUSCODE = STATUSRULE.ARTICLESTATUSCODE AND STATUSRULECOMBINATION.LINENR = STATUSRULE.LINENR` |

## Indexes

- `STATUSRULEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ARTICLESTATUSCOMPANYCODE,
       t.ARTICLESTATUSITEMTYPECODE,
       t.ARTICLESTATUSCODE,
       t.LINENR,
       t.SEQUENCE,
       t.ISPROTOTYPE,
       t.MANAGEKEY1,
       t.MANAGEKEY2,
       t.MANAGEKEY3,
       t.MANAGEKEY4,
       t.MANAGEKEY5,
       t.MANAGEKEY6
FROM   DB2ADMIN.STATUSRULE t
FETCH FIRST 100 ROWS ONLY;
```
