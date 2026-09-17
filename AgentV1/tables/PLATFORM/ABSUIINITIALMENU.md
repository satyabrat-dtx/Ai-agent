# DB2ADMIN.ABSUIINITIALMENU

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `UITYPE`, `USERUSERID`, `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 7 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 31957

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `USERUSERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `MENUCODE` | CHAR(20) |  | FK | foreign_key |  |
| 3 | `MENU2CODE` | CHAR(20) |  | FK | foreign_key |  |
| 4 | `MENU3CODE` | CHAR(20) |  | FK | foreign_key |  |
| 5 | `MENU4CODE` | CHAR(20) |  | FK | foreign_key |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `UITYPE` | INTEGER | NOT NULL | PK | primary_key |  |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `PROCESS1CODE` | CHAR(50) |  | FK | foreign_key |  |
| 15 | `PROCESS2CODE` | CHAR(50) |  | FK | foreign_key |  |
| 16 | `PROCESS3CODE` | CHAR(50) |  | FK | foreign_key |  |

## References (this table → parent) — 7

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSUIMENU_MENU` | `MENUCODE` | [`ABSUIMENU`](../PLATFORM/ABSUIMENU.md) | `CODE` | RESTRICT | `ABSUIINITIALMENU.MENUCODE = ABSUIMENU.CODE` |
| `ABSUIMENU_MENU2` | `MENU2CODE` | [`ABSUIMENU`](../PLATFORM/ABSUIMENU.md) | `CODE` | RESTRICT | `ABSUIINITIALMENU.MENU2CODE = ABSUIMENU.CODE` |
| `ABSUIMENU_MENU3` | `MENU3CODE` | [`ABSUIMENU`](../PLATFORM/ABSUIMENU.md) | `CODE` | RESTRICT | `ABSUIINITIALMENU.MENU3CODE = ABSUIMENU.CODE` |
| `ABSUIMENU_MENU4` | `MENU4CODE` | [`ABSUIMENU`](../PLATFORM/ABSUIMENU.md) | `CODE` | RESTRICT | `ABSUIINITIALMENU.MENU4CODE = ABSUIMENU.CODE` |
| `ABSUIPROCESS_PROCESS1` | `PROCESS1CODE` | [`ABSUIPROCESS`](../PLATFORM/ABSUIPROCESS.md) | `CODE` | RESTRICT | `ABSUIINITIALMENU.PROCESS1CODE = ABSUIPROCESS.CODE` |
| `ABSUIPROCESS_PROCESS2` | `PROCESS2CODE` | [`ABSUIPROCESS`](../PLATFORM/ABSUIPROCESS.md) | `CODE` | RESTRICT | `ABSUIINITIALMENU.PROCESS2CODE = ABSUIPROCESS.CODE` |
| `ABSUIPROCESS_PROCESS3` | `PROCESS3CODE` | [`ABSUIPROCESS`](../PLATFORM/ABSUIPROCESS.md) | `CODE` | RESTRICT | `ABSUIINITIALMENU.PROCESS3CODE = ABSUIPROCESS.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSUIINITIALMENUUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.USERUSERID,
       t.COMPANYCODE,
       t.MENUCODE,
       t.MENU2CODE,
       t.MENU3CODE,
       t.MENU4CODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.UITYPE
FROM   DB2ADMIN.ABSUIINITIALMENU t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
