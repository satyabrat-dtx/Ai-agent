# DB2ADMIN.WRKORDERPACKING

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 45
- **Primary key**: `COMPANYCODE`, `ORDPACKINGSALORDERCOUNTERCODE`, `ORDPACKINGSALESORDERCODE`, `ORDPACKINGORDERLINE`, `ORDPACKINGORDERSUBLINE`, `ORDPACKINGCOMPONENTORDERLINE`, `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 128468

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `ORDPACKINGSALORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `ORDPACKINGSALESORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `ORDPACKINGORDERLINE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 5 | `ORDPACKINGORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 6 | `ORDPACKINGCOMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 7 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 8 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 9 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 11 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `LOTNO` | CHAR(35) |  |  |  |  |
| 21 | `CARTONFROM` | DECIMAL(5,0) |  |  |  |  |
| 22 | `CARTONTO` | DECIMAL(5,0) |  |  |  |  |
| 23 | `COLORCODE` | CHAR(10) |  |  |  |  |
| 24 | `SIZECODE` | CHAR(10) |  |  |  |  |
| 25 | `PACKINGGROUP` | CHAR(3) |  |  |  |  |
| 26 | `PACKINGTYPE` | CHAR(1) |  |  |  |  |
| 27 | `LENGTH` | DECIMAL(7,2) |  |  |  |  |
| 28 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `BALANCEQTY` | DECIMAL(15,5) |  |  |  |  |
| 30 | `LINETOEXPLODE` | INTEGER | NOT NULL |  |  |  |
| 31 | `TIERWEIGHT` | DECIMAL(9,5) |  |  |  |  |
| 32 | `WEIGHTQTY` | DECIMAL(15,5) |  |  |  |  |
| 33 | `WIDTH` | DECIMAL(7,2) |  |  |  |  |
| 34 | `GROSSWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 35 | `FLAG` | CHAR(1) |  |  |  |  |
| 36 | `PRIORITY` | DECIMAL(3,0) |  |  |  |  |
| 37 | `NETWEIGHTQTY` | DECIMAL(15,5) |  |  |  |  |
| 38 | `HEIGHT` | DECIMAL(7,2) |  |  |  |  |
| 39 | `TOBECREATED` | INTEGER | NOT NULL |  |  |  |
| 40 | `YOURREFERENCE` | VARCHAR(200) |  |  |  |  |
| 41 | `SELECTED` | INTEGER | NOT NULL |  |  |  |
| 42 | `PROGRAMMENAME` | INTEGER | NOT NULL |  |  |  |
| 43 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 44 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKORDERPACKINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.ORDPACKINGSALORDERCOUNTERCODE,
       t.ORDPACKINGSALESORDERCODE,
       t.ORDPACKINGORDERLINE,
       t.ORDPACKINGORDERSUBLINE,
       t.ORDPACKINGCOMPONENTORDERLINE,
       t.LINENO,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02
FROM   DB2ADMIN.WRKORDERPACKING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
