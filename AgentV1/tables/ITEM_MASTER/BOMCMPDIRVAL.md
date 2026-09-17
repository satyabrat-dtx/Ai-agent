# DB2ADMIN.BOMCMPDIRVAL

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'BOM')
- **Roles**: `business_data`
- **Columns**: 35
- **Primary key**: `BOMCMP`, `BOMNID`, `BOMSEQ`, `BOMSS`, `BOMCMPDTM`, `INSUBCODE01`, `INSUBCODE02`, `INSUBCODE03`, `INSUBCODE04`, `INSUBCODE05`, `INSUBCODE06`, `INSUBCODE07`, `INSUBCODE08`, `INSUBCODE09`, `INSUBCODE10`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 198905

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BOMCMP` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `BOMNID` | DECIMAL(11,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `BOMSEQ` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `BOMSS` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `BOMCMPDTM` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `INSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 6 | `INSUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 7 | `INSUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 8 | `INSUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 9 | `INSUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 10 | `INSUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 11 | `INSUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 12 | `INSUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 13 | `INSUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 14 | `INSUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 15 | `OUTSUBCODE01` | CHAR(20) |  |  |  |  |
| 16 | `OUTSUBCODE02` | CHAR(10) |  |  |  |  |
| 17 | `OUTSUBCODE03` | CHAR(10) |  |  |  |  |
| 18 | `OUTSUBCODE04` | CHAR(10) |  |  |  |  |
| 19 | `OUTSUBCODE05` | CHAR(10) |  |  |  |  |
| 20 | `OUTSUBCODE06` | CHAR(10) |  |  |  |  |
| 21 | `OUTSUBCODE07` | CHAR(10) |  |  |  |  |
| 22 | `OUTSUBCODE08` | CHAR(10) |  |  |  |  |
| 23 | `OUTSUBCODE09` | CHAR(10) |  |  |  |  |
| 24 | `OUTSUBCODE10` | CHAR(10) |  |  |  |  |
| 25 | `OUTSKIPBOMCOMPONENT` | SMALLINT | NOT NULL |  |  |  |
| 26 | `OUTQUANTITYPER` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 27 | `OUTWASTE1` | DECIMAL(11,2) | NOT NULL |  |  |  |
| 28 | `OUTRESERVATIONWHSCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 29 | `OUTRESERVATIONWAREHOUSECODE` | CHAR(8) |  | FK | foreign_key |  |
| 30 | `OUTPRICE` | DECIMAL(18,5) |  |  |  |  |
| 31 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 32 | `OUTREFERENCEPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 33 | `OUTSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 34 | `OUTVARIANTCODE` | CHAR(20) |  |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BOMCMPDIRTMP_VALUE` | `BOMCMP`, `BOMNID`, `BOMSEQ`, `BOMSS`, `BOMCMPDTM` | [`BOMCMPDIRTMP`](../ITEM_MASTER/BOMCMPDIRTMP.md) | `BOMCMP`, `BOMNID`, `BOMSEQ`, `BOMSS`, `DIRECTIVETEMPLATECODE` | RESTRICT | `BOMCMPDIRVAL.BOMCMP = BOMCMPDIRTMP.BOMCMP AND BOMCMPDIRVAL.BOMNID = BOMCMPDIRTMP.BOMNID AND BOMCMPDIRVAL.BOMSEQ = BOMCMPDIRTMP.BOMSEQ AND BOMCMPDIRVAL.BOMSS = BOMCMPDIRTMP.BOMSS AND BOMCMPDIRVAL.BOMCMPDTM = BOMCMPDIRTMP.DIRECTIVETEMPLATECODE` |
| `LOGICALWAREHOUSE_OUTRESERVATIONWAREHOUSE` | `OUTRESERVATIONWHSCOMPANYCODE`, `OUTRESERVATIONWAREHOUSECODE` | [`LOGICALWAREHOUSE`](../WAREHOUSE/LOGICALWAREHOUSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BOMCMPDIRVAL.OUTRESERVATIONWHSCOMPANYCODE = LOGICALWAREHOUSE.COMPANYCODE AND BOMCMPDIRVAL.OUTRESERVATIONWAREHOUSECODE = LOGICALWAREHOUSE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BOMCMPDIRVALUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.BOMCMP,
       t.BOMNID,
       t.BOMSEQ,
       t.BOMSS,
       t.BOMCMPDTM,
       t.INSUBCODE01,
       t.INSUBCODE02,
       t.INSUBCODE03,
       t.INSUBCODE04,
       t.INSUBCODE05,
       t.INSUBCODE06,
       t.INSUBCODE07
FROM   DB2ADMIN.BOMCMPDIRVAL t
FETCH FIRST 100 ROWS ONLY;
```
