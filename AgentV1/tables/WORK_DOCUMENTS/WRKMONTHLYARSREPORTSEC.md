# DB2ADMIN.WRKMONTHLYARSREPORTSEC

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 97
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `EMPLOYEECODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 163278

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `EMPLOYEECODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 3 | `ATTENDANCECODESEC1` | CHAR(3) |  |  |  |  |
| 4 | `ATTENDANCECODESEC2` | CHAR(3) |  |  |  |  |
| 5 | `ATTENDANCECODESEC3` | CHAR(3) |  |  |  |  |
| 6 | `ATTENDANCECODESEC4` | CHAR(3) |  |  |  |  |
| 7 | `ATTENDANCECODESEC5` | CHAR(3) |  |  |  |  |
| 8 | `ATTENDANCECODESEC6` | CHAR(3) |  |  |  |  |
| 9 | `ATTENDANCECODESEC7` | CHAR(3) |  |  |  |  |
| 10 | `ATTENDANCECODESEC8` | CHAR(3) |  |  |  |  |
| 11 | `ATTENDANCECODESEC9` | CHAR(3) |  |  |  |  |
| 12 | `ATTENDANCECODESEC10` | CHAR(3) |  |  |  |  |
| 13 | `ATTENDANCECODESEC11` | CHAR(3) |  |  |  |  |
| 14 | `ATTENDANCECODESEC12` | CHAR(3) |  |  |  |  |
| 15 | `ATTENDANCECODESEC13` | CHAR(3) |  |  |  |  |
| 16 | `ATTENDANCECODESEC14` | CHAR(3) |  |  |  |  |
| 17 | `ATTENDANCECODESEC15` | CHAR(3) |  |  |  |  |
| 18 | `ATTENDANCECODESEC16` | CHAR(3) |  |  |  |  |
| 19 | `ATTENDANCECODESEC17` | CHAR(3) |  |  |  |  |
| 20 | `ATTENDANCECODESEC18` | CHAR(3) |  |  |  |  |
| 21 | `ATTENDANCECODESEC19` | CHAR(3) |  |  |  |  |
| 22 | `ATTENDANCECODESEC20` | CHAR(3) |  |  |  |  |
| 23 | `ATTENDANCECODESEC21` | CHAR(3) |  |  |  |  |
| 24 | `ATTENDANCECODESEC22` | CHAR(3) |  |  |  |  |
| 25 | `ATTENDANCECODESEC23` | CHAR(3) |  |  |  |  |
| 26 | `ATTENDANCECODESEC24` | CHAR(3) |  |  |  |  |
| 27 | `ATTENDANCECODESEC25` | CHAR(3) |  |  |  |  |
| 28 | `ATTENDANCECODESEC26` | CHAR(3) |  |  |  |  |
| 29 | `ATTENDANCECODESEC27` | CHAR(3) |  |  |  |  |
| 30 | `ATTENDANCECODESEC28` | CHAR(3) |  |  |  |  |
| 31 | `ATTENDANCECODESEC29` | CHAR(3) |  |  |  |  |
| 32 | `ATTENDANCECODESEC30` | CHAR(3) |  |  |  |  |
| 33 | `ATTENDANCECODESEC31` | CHAR(3) |  |  |  |  |
| 34 | `NUMBEROFHRSSEC1` | DECIMAL(5,2) |  |  |  |  |
| 35 | `NUMBEROFHRSSEC2` | DECIMAL(5,2) |  |  |  |  |
| 36 | `NUMBEROFHRSSEC3` | DECIMAL(5,2) |  |  |  |  |
| 37 | `NUMBEROFHRSSEC4` | DECIMAL(5,2) |  |  |  |  |
| 38 | `NUMBEROFHRSSEC5` | DECIMAL(5,2) |  |  |  |  |
| 39 | `NUMBEROFHRSSEC6` | DECIMAL(5,2) |  |  |  |  |
| 40 | `NUMBEROFHRSSEC7` | DECIMAL(5,2) |  |  |  |  |
| 41 | `NUMBEROFHRSSEC8` | DECIMAL(5,2) |  |  |  |  |
| 42 | `NUMBEROFHRSSEC9` | DECIMAL(5,2) |  |  |  |  |
| 43 | `NUMBEROFHRSSEC10` | DECIMAL(5,2) |  |  |  |  |
| 44 | `NUMBEROFHRSSEC11` | DECIMAL(5,2) |  |  |  |  |
| 45 | `NUMBEROFHRSSEC12` | DECIMAL(5,2) |  |  |  |  |
| 46 | `NUMBEROFHRSSEC13` | DECIMAL(5,2) |  |  |  |  |
| 47 | `NUMBEROFHRSSEC14` | DECIMAL(5,2) |  |  |  |  |
| 48 | `NUMBEROFHRSSEC15` | DECIMAL(5,2) |  |  |  |  |
| 49 | `NUMBEROFHRSSEC16` | DECIMAL(5,2) |  |  |  |  |
| 50 | `NUMBEROFHRSSEC17` | DECIMAL(5,2) |  |  |  |  |
| 51 | `NUMBEROFHRSSEC18` | DECIMAL(5,2) |  |  |  |  |
| 52 | `NUMBEROFHRSSEC19` | DECIMAL(5,2) |  |  |  |  |
| 53 | `NUMBEROFHRSSEC20` | DECIMAL(5,2) |  |  |  |  |
| 54 | `NUMBEROFHRSSEC21` | DECIMAL(5,2) |  |  |  |  |
| 55 | `NUMBEROFHRSSEC22` | DECIMAL(5,2) |  |  |  |  |
| 56 | `NUMBEROFHRSSEC23` | DECIMAL(5,2) |  |  |  |  |
| 57 | `NUMBEROFHRSSEC24` | DECIMAL(5,2) |  |  |  |  |
| 58 | `NUMBEROFHRSSEC25` | DECIMAL(5,2) |  |  |  |  |
| 59 | `NUMBEROFHRSSEC26` | DECIMAL(5,2) |  |  |  |  |
| 60 | `NUMBEROFHRSSEC27` | DECIMAL(5,2) |  |  |  |  |
| 61 | `NUMBEROFHRSSEC28` | DECIMAL(5,2) |  |  |  |  |
| 62 | `NUMBEROFHRSSEC29` | DECIMAL(5,2) |  |  |  |  |
| 63 | `NUMBEROFHRSSEC30` | DECIMAL(5,2) |  |  |  |  |
| 64 | `NUMBEROFHRSSEC31` | DECIMAL(5,2) |  |  |  |  |
| 65 | `LEAVECODESEC1` | CHAR(3) |  |  |  |  |
| 66 | `LEAVECODESEC2` | CHAR(3) |  |  |  |  |
| 67 | `LEAVECODESEC3` | CHAR(3) |  |  |  |  |
| 68 | `LEAVECODESEC4` | CHAR(3) |  |  |  |  |
| 69 | `LEAVECODESEC5` | CHAR(3) |  |  |  |  |
| 70 | `LEAVECODESEC6` | CHAR(3) |  |  |  |  |
| 71 | `LEAVECODESEC7` | CHAR(3) |  |  |  |  |
| 72 | `LEAVECODESEC8` | CHAR(3) |  |  |  |  |
| 73 | `LEAVECODESEC9` | CHAR(3) |  |  |  |  |
| 74 | `LEAVECODESEC10` | CHAR(3) |  |  |  |  |
| 75 | `LEAVECODESEC11` | CHAR(3) |  |  |  |  |
| 76 | `LEAVECODESEC12` | CHAR(3) |  |  |  |  |
| 77 | `LEAVECODESEC13` | CHAR(3) |  |  |  |  |
| 78 | `LEAVECODESEC14` | CHAR(3) |  |  |  |  |
| 79 | `LEAVECODESEC15` | CHAR(3) |  |  |  |  |
| 80 | `LEAVECODESEC16` | CHAR(3) |  |  |  |  |
| 81 | `LEAVECODESEC17` | CHAR(3) |  |  |  |  |
| 82 | `LEAVECODESEC18` | CHAR(3) |  |  |  |  |
| 83 | `LEAVECODESEC19` | CHAR(3) |  |  |  |  |
| 84 | `LEAVECODESEC20` | CHAR(3) |  |  |  |  |
| 85 | `LEAVECODESEC21` | CHAR(3) |  |  |  |  |
| 86 | `LEAVECODESEC22` | CHAR(3) |  |  |  |  |
| 87 | `LEAVECODESEC23` | CHAR(3) |  |  |  |  |
| 88 | `LEAVECODESEC24` | CHAR(3) |  |  |  |  |
| 89 | `LEAVECODESEC25` | CHAR(3) |  |  |  |  |
| 90 | `LEAVECODESEC26` | CHAR(3) |  |  |  |  |
| 91 | `LEAVECODESEC27` | CHAR(3) |  |  |  |  |
| 92 | `LEAVECODESEC28` | CHAR(3) |  |  |  |  |
| 93 | `LEAVECODESEC29` | CHAR(3) |  |  |  |  |
| 94 | `LEAVECODESEC30` | CHAR(3) |  |  |  |  |
| 95 | `LEAVECODESEC31` | CHAR(3) |  |  |  |  |
| 96 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKMONTHLYARSREPORTSECUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.EMPLOYEECODE,
       t.ATTENDANCECODESEC1,
       t.ATTENDANCECODESEC2,
       t.ATTENDANCECODESEC3,
       t.ATTENDANCECODESEC4,
       t.ATTENDANCECODESEC5,
       t.ATTENDANCECODESEC6,
       t.ATTENDANCECODESEC7,
       t.ATTENDANCECODESEC8,
       t.ATTENDANCECODESEC9
FROM   DB2ADMIN.WRKMONTHLYARSREPORTSEC t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
